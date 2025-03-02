from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.signals import post_delete

from .signals import delete_cache_total_sum
from .tasks import set_price, set_comment, test_task

# внутри контейнера код запускается относительно service, и там clients находится в корне
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()


    # я кажется неправильно понимал суть инит... ну теперь ясно, модель орм это класс джанго, когда он создаётся он
    # инициализирует поля и заносит данные полученные из бд затем вызывается метод super().save(*args, **kwargs) и
    # модель сохраняется с переданными значениями, получается у нас есть время перед сохранением записи чтобы добавить
    # кастомную логику в __init__ и есть возможность переопределить save() а так же есть сигналы чтобы реализовать
    # логику перед\после сохранения\удаления... я неправильно понимал метод init я думал что создание подразумевает
    # само создание записи в бд, а это оказывается создание класса модели и оно происходит и при созд.
    # записи и при извлечении записи из бд
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # во время создания записи присваиваем значение скидки переменной self.__full_price для того чтобы
        # отслеживать изменение поля discount_percent и пересчитывать поле price в модели Subscription
        self.__full_price = self.full_price

    def save(self, *args, **kwargs):
        # при сохранении модели проверяем изменилась ли скидка и если да то пересчитываем
        # скидку в связанных моделях Subscriptions
        if self.full_price != self.__full_price:
            for subscription in self.subscriptions.all():
                # Когда вы вызываете delay, задача помещается в очередь, и Celery выполняет её позже, при этом ваш
                # основной процесс продолжает работу, не ожидая завершения этой задачи
                set_price.delay(subscription.id)
                set_comment.delay(subscription.id)

        return super().save(*args, **kwargs)

class Plan(models.Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_type = models.CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # во время создания (извлечения из бд) записи присваиваем значение скидки переменной self.__discount_percent для
        # того чтобы отслеживать изменение поля discount_percent и пересчитывать поле price в модели Subscription
        self.__discount_percent = self.discount_percent

    def save(self, *args, **kwargs):
        # при сохранении модели проверяем изменилась ли скидка и если да то пересчитываем
        # скидку в связанных моделях Subscriptions
        if self.discount_percent != self.__discount_percent:
            for subscription in self.subscriptions.all():
                # Когда вы вызываете delay, задача помещается в очередь, и Celery выполняет её позже, при этом ваш
                # основной процесс продолжает работу, не ожидая завершения этой задачи
                set_price.delay(subscription.id)
                set_comment.delay(subscription.id)


        return super().save(*args, **kwargs)

    def get_old_disc(self):
        return self.__discount_percent

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)
    price = models.PositiveSmallIntegerField(default=0)
    # ХЭШ ИНДЕКС, БРИН ИНДЕКС, БИТРИ ИНДЕКС
    # индексы нужно устанавливать на поля по которым происходит поиск, если поиск происходит по двум
    # полям следует установить составной индекс
    comment = models.CharField(max_length=50, default='', db_index=True)

    field_a = models.CharField(max_length=50, blank=True, default='')
    field_b = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        # индексируем сочетание двух полей. составной индекс,
        indexes = [
            models.Index(fields=['field_a', 'field_b'])
        ]

    def save(self, *args, save_model=True, **kwargs):
        ''' во время создания новой записи запускаем таск пересчёта цены'''

        # если обьект создаётся то у него нет self.id
        creating = not bool(self.id)
        # вызываем метод save класса супер чтобы сохранить обьект (если он создаётся то в этот момент присвоится id)
        result = super().save(*args, **kwargs)
        # и в случае если обьект создаётся тогда запускаем таску подсчёта полной стоимости
        if creating:
            set_price.delay(self.id)
            test_task.delay()
        return result

