import django_filters
from .models import CurrencyExchangeRate

class CurrencyExchangeRateFilter(django_filters.FilterSet):
    base_currency = django_filters.CharFilter(field_name='base_currency__code', lookup_expr='exact')
    quote_currency = django_filters.CharFilter(field_name='quote_currency__code', lookup_expr='exact')
    
    class Meta:
        model = CurrencyExchangeRate
        fields = {
            'base_currency': ['exact'],
            'quote_currency': ['exact'],
            'exchange_rate': ['gte', 'lte'],
            'date': ['exact', 'gte', 'lte'],
        }