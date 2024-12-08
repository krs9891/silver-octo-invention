from django.contrib import admin
from api.models import Currency, CurrencyExchangeRate
from django.http import HttpResponse
import openpyxl

class CurrencyPairFilter(admin.SimpleListFilter):
    title = 'currency pair'
    parameter_name = 'currency_pair'

    def lookups(self, request, model_admin):
        pairs = set(
            CurrencyExchangeRate.objects.values_list(
                'base_currency__code', 'quote_currency__code'
            )
        )
        return [(f"{base}{quote}", f"{base}{quote}") for base, quote in pairs]

    def queryset(self, request, queryset):
        if self.value():
            base, quote = self.value()[:3], self.value()[3:]
            return queryset.filter(base_currency__code=base, quote_currency__code=quote)
        return queryset

class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['currency_pair', 'exchange_rate', 'date']
    list_filter = [CurrencyPairFilter, 'date']
    actions = ['export_to_xlsx']
    ordering = ['-date']

    def export_to_xlsx(self, request, queryset):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        sheet.append(["Currency Pair", "Exchange Rate", "Date"])
        
        for rate in queryset:
            sheet.append([rate.currency_pair(), round(rate.exchange_rate, 3), rate.date])

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = 'attachment; filename="currency_rates.xlsx"'
        workbook.save(response)
        return response

    export_to_xlsx.short_description = "Export selected to XLSX"

admin.site.register(Currency)
admin.site.register(CurrencyExchangeRate, CurrencyExchangeRateAdmin)
