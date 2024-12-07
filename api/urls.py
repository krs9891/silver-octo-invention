from django.urls import path
from .views import CurrencyExchangeView

urlpatterns = [
    path('<str:base_currency>/<str:quote_currency>/', CurrencyExchangeView.as_view()),
]
