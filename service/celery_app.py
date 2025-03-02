import os
import time
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


# запустить таск через селери debug_task.delay()

# # # указываем файл настроек в переменню окружения
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')
#
# # Создаёт экземп. прилож. Celery с именем 'service', чаще всего совпадает с названием Django-проекта, но не обязательно
# app = Celery('service')
# # Загружает конфигурацию Celery из Django-настроек (settings.py), например CELERY_BROKER_URL
# app.config_from_object('django.conf:settings')
# # Явно задаёт адрес брокера (очереди задач), settings.CELERY_BROKER_URL — это строка в settings.py
# app.conf.broker_url = settings.CELERY_BROKER_URL
# # Автоматически ищет файлы с задачами (tasks.py)
# app.autodiscover_tasks()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL

app.conf.beat_schedule = settings.CELERY_BEAT_SCHEDULE
# sdfsdfsfdfgdfg


# Указываем расписание
# app.conf.beat_schedule = {
#     'task_good': {
#         'task': 'services.tasks.task_good',
#         'schedule': timedelta(seconds=5),  # Каждые 5 секунд
#     },
# }
# app.conf.beat_schedule = {
#     "task_print": {
#         "task": "services.tasks.task_print",
#         "schedule": crontab(minute="*/1"),  # Каждую минуту
#     },
#     'task_good': {
#         'task': 'services.tasks.task_good',
#         'schedule': timedelta(seconds=5),  # Каждые 5 секунд
#     },
#     'test_task': {
#         'task': 'services.tasks.test_task',
#         'schedule': timedelta(seconds=5),
#     },
#     'set_price': {
#         'task': 'services.tasks.set_price',
#         'schedule': timedelta(seconds=5),
#     }
# }


app.autodiscover_tasks()
