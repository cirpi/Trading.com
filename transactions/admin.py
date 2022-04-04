from django.contrib import admin
from .models import Asset, Stock, Balance


# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Asset)
admin.site.register(Stock, StockAdmin)
admin.site.register(Balance)
