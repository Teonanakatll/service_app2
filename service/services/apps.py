from django.apps import AppConfig
from django.db.models.signals import post_delete

from services.signals import delete_cache_total_sum


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    def ready(self):
        from .models import Subscription
        # delete_cache_total_sum - наш сигнал (receiver) из signals.py
        # Это исключает использование декоратора @receiver, так как ты и так вручную подключаешь сигнал с помощью метода connect
        post_delete.connect(delete_cache_total_sum, sender=Subscription)