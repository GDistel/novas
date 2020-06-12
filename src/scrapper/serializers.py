from rest_framework import serializers
from .models import CotoProductModel, CotoProductPriceUpdateModel

class CotoProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CotoProductModel
        fields = (
            'number',
            'name',
            'bulk_purchase_amount',
            'bulk_purchase_measure',
            'categories_path',
            'image_url',
            'link',
            'created',
            'last_modified',
            'url',
            'price_updates'
        )

class CotoProductPriceUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CotoProductPriceUpdateModel
        fields = (
            'product',
            'unit_price',
            'promo_required_amount',
            'promo_unit_price',
            'text_price_discount',
            'bulk_purchase_price',
            'update_date',
            'url'
        )