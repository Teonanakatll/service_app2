from django.core.validators import MaxValueValidator
from django.db import models
from . tasks import set_price

# внутри контейнера код запускается относительно service, и там clients находится в корне
from clients.models import Client


class Service(models.Model):
    name = models.CharField(max_length=50)
    full_price = models.PositiveIntegerField()

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
                set_price.delay(subscription.id)

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
        # во время создания записи присваиваем значение скидки переменной self.__discount_percent для того чтобы
        # отслеживать изменение поля discount_percent и пересчитывать поле price в модели Subscription
        self.__discount_percent = self.discount_percent

    def save(self, *args, **kwargs):
        # при сохранении модели проверяем изменилась ли скидка и если да то пересчитываем
        # скидку в связанных моделях Subscriptions
        if self.discount_percent != self.__discount_percent:
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)

        return super().save(*args, **kwargs)

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.PROTECT)
    service = models.ForeignKey(Service, related_name='subscriptions', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, related_name='subscriptions', on_delete=models.PROTECT)
    price = models.PositiveSmallIntegerField(default=0)

    # этот вариант неправильный так как пересчёт цены одлжен происходить не в момент сохранения продписки
    # а в момент изменения цены в модели Service или скидки в модели Plan
    # def save(self, *args, save_model=True, **kwargs):
    #     if save_model:
    #         set_price.delay(self.id)
    #
    #     return super().save(*args, **kwargs)
