# api/management/commands/delete_all_records.py
from django.core.management.base import BaseCommand
from api.models import Currency, CurrencyExchangeRate

class Command(BaseCommand):
    help = "Delete all records from the database"

    def handle(self, *args, **kwargs):
        CurrencyExchangeRate.objects.all().delete()
        Currency.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Successfully deleted all records."))