from django.core.management.base import BaseCommand
import yfinance as yf
from api.models import Currency, CurrencyExchangeRate

class Command(BaseCommand):
    help = "Fetch initial currency data"

    def handle(self, *args, **kwargs):
        pairs = ["EURUSD=X", "USDJPY=X", "PLNUSD=X", "PLNEUR=X", "PLNCHF=X", "PLNGBP=X", "EURGBP=X"]

        for pair in pairs:
            ticker = yf.Ticker(pair)
            data = ticker.history(period="1y", interval="1d")  # Fetch data for the past year with daily intervals

            if not data.empty:
                base, quote = pair.split('=')[0].split('X')[0][:3], pair.split('=')[0].split('X')[0][3:]

                base_currency, _ = Currency.objects.get_or_create(code=base)
                quote_currency, _ = Currency.objects.get_or_create(code=quote)

                for date, row in data.iterrows():
                    rate = row['Close']
                    CurrencyExchangeRate.objects.update_or_create(
                        base_currency=base_currency,
                        quote_currency=quote_currency,
                        date=date.date(),  # Ensure date is in the correct format
                        defaults={"exchange_rate": rate}
                    )

        self.stdout.write(self.style.SUCCESS("Successfully loaded currency rates."))
