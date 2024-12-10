from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from api.models import Currency, CurrencyExchangeRate
from api.filters import CurrencyExchangeRateFilter
from api.serializers import CurrencyExchangeRateSerializer
from django.db.models import Subquery, OuterRef

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
                serializer = CurrencyExchangeRateSerializer(rate)
                return Response(serializer.data)
            else:
                return Response({"error": "Currency pair not found"}, status=404)
        except Currency.DoesNotExist:
            return Response({"error": "Currency pair not found"}, status=404)

class CurrencyExchangeRateListView(generics.ListAPIView):
    queryset = CurrencyExchangeRate.objects.all()
    serializer_class = CurrencyExchangeRateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CurrencyExchangeRateFilter

    def get_queryset(self):
        latest_rates = CurrencyExchangeRate.objects.filter(
            base_currency=OuterRef('base_currency'),
            quote_currency=OuterRef('quote_currency')
        ).order_by('-date').values('date')[:1]

        queryset = CurrencyExchangeRate.objects.filter(date=Subquery(latest_rates))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)