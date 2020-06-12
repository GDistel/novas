from rest_framework import viewsets
from .serializers import CotoProductSerializer, CotoProductPriceUpdateSerializer
from .models import CotoProductModel, CotoProductPriceUpdateModel


class CotoProductsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed or edited
    """
    queryset = CotoProductModel.objects.all().order_by('-created')
    serializer_class = CotoProductSerializer

class CotoProductPriceUpdatesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows product price updates to be viewed or edited
    """
    queryset = CotoProductPriceUpdateModel.objects.all().order_by('-update_date')
    serializer_class = CotoProductPriceUpdateSerializer