from django.conf import settings
from django.core.cache import cache
# from django.db.models.signals import post_delete
# from django.dispatch import receiver


# sender — КЛАСС МОДЕЛИ, которая была сохранена.
# instance — ЭКЗЕМПЛЯР МОДЕЛИ, который был сохранен.
# created — булево значение, которое говорит, был ли объект только что создан или обновлен.
# raw — если сохранение происходило через "сырой" SQL запрос, то будет True, если через Django ORM — False.
# kwargs — дополнительный словарь с дополнительными параметрами, которые могут быть переданы в сигнал.

# После удаления из базы данных объект всё ещё существует в памяти на время работы функции обработчика post_delete

# @receiver(post_delete, sender=None)
# # так как модель Subscription уже удалена следовательно мы в ней не сможем вызвать инвалидацию кеша
def delete_cache_total_sum(*args, **kwargs):
    cache.delete(settings.PRICE_CACHE_NAME)