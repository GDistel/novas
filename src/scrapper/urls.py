from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import views

schema_view = get_schema_view(title='Coto Products API')

# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash = False)
router.register(r'coto_products', views.CotoProductsViewSet)
router.register(r'coto_product_price_updates', views.CotoProductPriceUpdatesViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view)
]
