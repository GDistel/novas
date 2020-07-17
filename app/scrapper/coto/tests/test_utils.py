from django.test import TestCase
import re
from bs4 import BeautifulSoup, element
from scrapper.models import CotoProductModel, CotoProductPriceUpdateModel
from ..utils import *

class UtilsTestCase(TestCase):
    def setUp(self):
        self.dummy_route = 'https://www.google.com'
        self.list_view_route = 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-bebidas-bebidas-con-alcohol-cerveza/_/N-137sk0z'
        self.detail_route = 'https://www.cotodigital3.com.ar/sitios/cdigi/producto/-cerveza--corona---porron-330-cc/_/A-00009696-00009696-200'
        self.detail_soup = get_detail_soup(self.detail_route)
        self.list_view_soup = get_soup(self.list_view_route)

    def test_get_soup(self):
        soup = get_soup(self.dummy_route)
        self.assertIsInstance(soup, BeautifulSoup)
    
    def test_get_detail_soup(self):
        result = get_detail_soup(self.detail_route)
        for soup in result:
            self.assertIsInstance(soup, element.Tag)
    
    def test_scrap_product_data(self):
        cleaned_product_data = scrap_product_data(self.detail_soup)
        product, created = CotoProductModel.objects.update_or_create(
            number = cleaned_product_data.get('number'),
            defaults = {
                'name': cleaned_product_data.get('name'),
                'bulk_purchase_amount': cleaned_product_data.get('bulk_purchase_amount'),
                'bulk_purchase_measure': cleaned_product_data.get('bulk_purchase_measure'),
                'categories_path': cleaned_product_data.get('categories_path'),
                'image_url': cleaned_product_data.get('image_url'),
                'link': self.detail_route
            }
        )
        priceUpdate = CotoProductPriceUpdateModel.objects.create(
            product = product,
            unit_price = cleaned_product_data.get('unit_price'),
            promo_required_amount = cleaned_product_data.get('promo_required_amount'),
            promo_unit_price = cleaned_product_data.get('promo_unit_price'),
            text_price_discount = cleaned_product_data.get('text_price_discount'),
            bulk_purchase_price = cleaned_product_data.get('bulk_purchase_price'),
        )
        self.assertIsInstance(product, CotoProductModel)
        self.assertIsInstance(priceUpdate, CotoProductPriceUpdateModel)
    
    def test_scrap_detail_routes(self):
        detail_routes = scrap_detail_routes(self.list_view_soup)
        self.assertIsInstance(detail_routes, list)

    def test_get_next_page_route(self):
        next_page_route = get_next_page_route(self.list_view_soup, 1)
        self.assertRegex(next_page_route, re.compile('^https?://.+'))