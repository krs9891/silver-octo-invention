from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Currency, CurrencyExchangeRate

class CurrencyExchangeView(APIView):
    def get(self, request, base_currency, quote_currency):
        try:
            base = Currency.objects.get(code=base_currency)
            quote = Currency.objects.get(code=quote_currency)
            rate = CurrencyExchangeRate.objects.filter(
                base_currency=base, 
                quote_currency=quote
            ).order_by('-date').first() 

            if rate:
                return Response({
                    "currency_pair": rate.currency_pair(),
                    "exchange_rate": round(rate.exchange_rate, 3)
                })
            else:
                return Response({"error": "Currency pair not found"}, status=404)
        except Currency.DoesNotExist:
            return Response({"error": "Currency pair not found"}, status=404)
