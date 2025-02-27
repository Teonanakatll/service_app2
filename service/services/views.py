from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from django.core.cache import cache
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
#
from django.conf import settings
from services.models import Subscription
from services.serializer import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().select_related('plan').prefetch_related(
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email'))
    )#.annotate(price=F('service__full_price') -
     #                F('service__full_price') * F('plan__discount_percent') / 100.00)
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        # пробуем взять total_price из кеша
        price_cache = cache.get(settings.PRICE_CACHE_NAME)

        if price_cache:
            total_price = price_cache
        # если такого значения в кеше нет вычисляем его и заносим в кеш
        else:
            total_price = queryset.aggregate(total=Sum('price')).get('total')
            cache.set(settings.PRICE_CACHE_NAME, total_price, 60 * 60)

        # данные ответа присваиваем словарю с ключом result
        response_data = {'result': response.data}
        # заменяем данные ответа нашим словарём
        response.data = response_data
        response_data['total_amount'] = total_price
        # добавляем свой ключ для присваивания данных агрегации

        return response

def photo_view(request):
    return render(request, 'services/photo.html')