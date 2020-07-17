from django.contrib import admin
from .models import CotoProductModel, CotoProductPriceUpdateModel
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter

class CotoProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'last_modified')
    list_filter = (
        ('category', ChoiceDropdownFilter),
    )

class CotoProductPriceUpdateModelAdmin(admin.ModelAdmin):
    readonly_fields = ('update_date',)

admin.site.register(CotoProductModel, CotoProductModelAdmin)
admin.site.register(CotoProductPriceUpdateModel, CotoProductPriceUpdateModelAdmin)
