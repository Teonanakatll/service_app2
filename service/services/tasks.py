from celery import shared_task
from django.db.models import F


@shared_task
def set_price(subscripion_id):
    from services.models import Subscription

    subscripion = Subscription.objects.filter(id=subscripion_id).annotate(annotated_price=F('service__full_price') -
                                        F('service__full_price') * F('plan__discount_percent') / 100.00).first()

    subscripion.price = subscripion.annotated_price
    # save_mode=False - так как таска вызывает save модели а сейв модели вызывает таску...
    subscripion.save()