from rest_framework import serializers
from api.models import CurrencyExchangeRate

class CurrencyExchangeRateSerializer(serializers.ModelSerializer):
    currency_pair = serializers.SerializerMethodField()
    exchange_rate = serializers.SerializerMethodField()

    class Meta:
        model = CurrencyExchangeRate
        fields = ['currency_pair', 'exchange_rate']

    def get_currency_pair(self, obj):
        return obj.currency_pair()

    def get_exchange_rate(self, obj):
        return round(obj.exchange_rate, 3)