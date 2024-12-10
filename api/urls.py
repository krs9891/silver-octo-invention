from django.urls import path
from .views import CurrencyExchangeView, CurrencyExchangeRateListView

urlpatterns = [
    path('<str:base_currency>/<str:quote_currency>/', CurrencyExchangeView.as_view(), name='currency-exchange-rate'),
    path('', CurrencyExchangeRateListView.as_view(), name='currency_exchange_rate_list'),
]
