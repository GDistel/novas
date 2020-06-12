from django.db import models

class CotoProductModel(models.Model):
    number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=False, null=True, blank=True)
    bulk_purchase_amount = models.PositiveIntegerField(unique=False, null=True, blank=True)
    bulk_purchase_measure = models.CharField(max_length=255, unique=False, null=True, blank=True)
    categories_path = models.CharField(max_length=255, unique=False, null=True, blank=True)
    image_url = models.URLField(unique=False, null=True, blank=True)
    link = models.URLField(unique=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False) 

    def __str__(self):
        return f'{self.number} - {self.name}'

class CotoProductPriceUpdateModel(models.Model):
    product = models.ForeignKey(CotoProductModel, on_delete=models.CASCADE, related_name='price_updates')
    unit_price = models.FloatField(null=True, blank=True)
    promo_required_amount = models.PositiveIntegerField(unique=False, null=True, blank=True)
    promo_unit_price = models.FloatField(max_length=255, unique=False, null=True, blank=True)
    text_price_discount = models.CharField(max_length=255, unique=False, null=True, blank=True)
    bulk_purchase_price = models.FloatField(null=True, blank=True)

    update_date = models.DateTimeField(auto_now_add=True, editable=False, null=False)

    def __str__(self):
        return f'Product: {self.product.number} - updated on {self.update_date}'