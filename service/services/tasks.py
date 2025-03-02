import datetime
import time
from celery_app import app
from celery import shared_task
from django.conf import settings
from django.core.cache import cache
from django.db import transaction
from django.db.models import F
# from сelery_singleton import Singleton
from celery_singleton import Singleton

# при изменении тасков нужно перезагрузить docker, celery сам не перезагружается
# Singleton - ориентируется на переданное id и если таска с таким аргументом есть он не создасе новую
@shared_task(base=Singleton)
def set_price(subscription_id):
    from services.models import Subscription

    # чтобы избавиться от проблемы паралельной работы разных тасок над одним экзэмпляром модели бд
    with transaction.atomic():

        # Метод select_for_update() используется в Django ORM для блокировки строк в базе данных на время выполнения
        # транзакции. Это помогает избежать проблем с конкуренцией и гарантирует, что только один процесс или
        # пользователь может изменить определённые строки в базе данных в рамках одной транзакции
        subscription = Subscription.objects.select_for_update().filter(id=subscription_id).annotate(annotated_price=F('service__full_price') -
                                            F('service__full_price') * F('plan__discount_percent') / 100.00).first()


        subscription.price = subscription.annotated_price
        # save_mode=False - так как таска вызывает save модели а сейв модели вызывает таску...
        subscription.save()

    # Инвалидировать кеш — это процесс удаления или сброса данных, которые находятся в кеше, чтобы они больше не
    # использовались или не могли быть извлечены. Это может понадобиться, например, когда
    # данные изменяются и кешированные данные больше не актуальны, либо для освобождения памяти
    cache.delete(settings.PRICE_CACHE_NAME)

@shared_task(base=Singleton)
def set_comment(subscription_id):
    from services.models import Subscription

    # чтобы избавиться от проблемы паралельной работы разных тасок над одним экзэмпляром модели бд
    with transaction.atomic():
        # Метод select_for_update() используется в Django ORM для блокировки строк в базе данных на время выполнения
        # транзакции. Это помогает избежать проблем с конкуренцией и гарантирует, что только один процесс или
        # пользователь может изменить определённые строки в базе данных в рамках одной транзакции
        subscription = Subscription.objects.select_for_update().get(id=subscription_id)

        subscription.comment = str(datetime.datetime.now())
        # save_mode=False - так как таска вызывает save модели а сейв модели вызывает таску...
        subscription.save()

    # Инвалидировать кеш — это процесс удаления или сброса данных, которые находятся в кеше, чтобы они больше не
    # использовались или не могли быть извлечены. Это может понадобиться, например, когда
    # данные изменяются и кешированные данные больше не актуальны, либо для освобождения памяти
    ### логика в том чтобы удалить кеш при обновлении информации и получается при запроссе через вью списка записей
    # кеша не будет поэтому он заново вычислиться и присвоится с актуальным значением

@shared_task
def task_good():
    time.sleep(10)
    print('fffffffffffffffffffffffffffffffffff')

@shared_task
def task_print():

    print('1000')

@app.task()
def test_task():
    print("Тестовая задача выполнена!")

# app.conf.beat_schedule = {
#     "test": {
#         "task": 'services.tasks.test_task',
#         "schedule": time.timedelta(seconds=10),
#     },
# }