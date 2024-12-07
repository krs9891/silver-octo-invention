from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Currency, CurrencyExchangeRate
from datetime import date
from django.contrib.auth.models import User

class CurrencyExchangeRateTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_currency = Currency.objects.create(code='EUR')
        self.quote_currency = Currency.objects.create(code='USD')
        self.exchange_rate = CurrencyExchangeRate.objects.create(
            base_currency=self.base_currency,
            quote_currency=self.quote_currency,
            exchange_rate=1.058559536933899,
            date=date.today()
        )
        self.superuser = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin'
        )

    def test_get_currency_exchange_rate(self):
        url = reverse('currency-exchange-rate', args=['EUR', 'USD'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['currency_pair'], 'EURUSD')
        self.assertEqual(response.data['exchange_rate'], 1.059)

    def test_currency_pair_not_found(self):
        url = reverse('currency-exchange-rate', args=['EUR', 'JPY'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Currency pair not found')

    def test_base_currency_not_found(self):
        url = reverse('currency-exchange-rate', args=['ABC', 'USD'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Currency pair not found')

    def test_quote_currency_not_found(self):
        url = reverse('currency-exchange-rate', args=['EUR', 'XYZ'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Currency pair not found')

    def test_admin_login(self):
        login = self.client.login(username='admin', password='admin')
        self.assertTrue(login)

    def test_admin_currency_exchange_rate_list(self):
        self.client.login(username='admin', password='admin')
        url = reverse('admin:api_currencyexchangerate_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_currency_exchange_rate_export(self):
        self.client.login(username='admin', password='admin')
        url = reverse('admin:api_currencyexchangerate_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Select all records and perform the export action
        post_data = {
            'action': 'export_to_xlsx',
            '_selected_action': [self.exchange_rate.id]
        }
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="currency_rates.xlsx"')
