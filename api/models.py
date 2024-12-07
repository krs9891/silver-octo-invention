from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code


class CurrencyExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, related_name='base_currency', on_delete=models.CASCADE)
    quote_currency = models.ForeignKey(Currency, related_name='quote_currency', on_delete=models.CASCADE)
    exchange_rate = models.FloatField()
    date = models.DateField()

    class Meta:
        unique_together = ('base_currency', 'quote_currency', 'date')

    def __str__(self):
        return f"{self.base_currency}/{self.quote_currency} - {self.exchange_rate} on {self.date}"
