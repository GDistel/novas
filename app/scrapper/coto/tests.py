from django.test import TestCase
from bs4 import BeautifulSoup
from .cleaners import *

class CleanersTestCase(TestCase):
    def test_clean_string(self):
        dirty = '    This    is a     dirty string'
        cleaned = clean_string(dirty)
        self.assertEqual(cleaned, 'This is a dirty string')
    
    def test_unit_price(self):
        dirty = 'PRECIO CONTADO  $133.60'
        cleaned = unit_price(dirty)
        self.assertEqual(cleaned, 133.6)

    def test_capture_product_number(self):
        dirty = 'Queso  Gouda  (1234)'
        cleaned = capture_product_number(dirty)
        self.assertEqual(cleaned, '1234')
    
    def test_name_number(self):
        dirty = 'Queso  Gouda  (1234)'
        cleaned = name_number(dirty)
        self.assertEqual(cleaned, ('Queso Gouda', '1234'))
    
    def test_promo_required_amount(self):
        dirty = 'Llevando 3'
        cleaned = promo_required_amount(dirty)
        self.assertEqual(cleaned, 3)

    def test_promo_unit_price(self):
        dirty = '$4.63c/u'
        cleaned = promo_unit_price(dirty)
        self.assertEqual(cleaned, 4.63)

    def test_text_price_discount(self):
        dirty = '80\%  2da '
        cleaned = text_price_discount(dirty)
        self.assertEqual(cleaned, '80\% 2da')

    def test_bulk_purchase(self):
        dirty = 'Precio por 1 Litro : $4.28'
        cleaned = bulk_purchase(dirty)
        self.assertEqual(cleaned, (1, 'Litro ', 4.28))
        # Intentional trailing white space

    def test_categories_path(self):
        soup_a = BeautifulSoup('<p>Groceries</p>', 'html.parser')
        soup_b = BeautifulSoup('<p>Store</p>', 'html.parser')
        soup_c = BeautifulSoup('<p>Cheese</p>', 'html.parser')
        dirty = [soup_a, soup_b, soup_c]
        cleaned = categories_path(dirty)
        self.assertEqual(cleaned, 'Groceries > Store > Cheese')
    