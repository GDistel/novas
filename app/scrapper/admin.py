from django.contrib import admin
from .models import CotoProductModel, CotoProductPriceUpdateModel

class CotoProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'last_modified')

class CotoProductPriceUpdateModelAdmin(admin.ModelAdmin):
    readonly_fields = ('update_date',)

admin.site.register(CotoProductModel, CotoProductModelAdmin)
admin.site.register(CotoProductPriceUpdateModel, CotoProductPriceUpdateModelAdmin)