from django.contrib import admin
from api.models import Currency, CurrencyExchangeRate
from django.http import HttpResponse
import openpyxl

class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['currency_pair', 'exchange_rate', 'date']
    actions = ['export_to_xlsx']

    def export_to_xlsx(self, request, queryset):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        sheet.append(["Currency Pair", "Exchange Rate", "Date"])
        
        for rate in queryset:
            sheet.append([rate.currency_pair(), rate.exchange_rate, rate.date])

        response = HttpResponse(content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'attachment; filename="currency_rates.xlsx"'
        workbook.save(response)
        return response

    export_to_xlsx.short_description = "Export selected to XLSX"

admin.site.register(Currency)
admin.site.register(CurrencyExchangeRate, CurrencyExchangeRateAdmin)
