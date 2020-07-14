from django.test import TestCase
from scrapper.models import CotoProductModel, CotoProductPriceUpdateModel
from datetime import datetime

class CotoProductTestCase(TestCase):
    def setUp(self):
        CotoProductModel.objects.create(
            name = "Gouda Cheese",
            number = 123,
            bulk_purchase_amount = 2,
            bulk_purchase_measure = 'Kilograms',
            categories_path = 'frescos > queso > holandeses',
            image_url = 'https://www.google.com',
            link = 'https://www.google.com'
        )

    def test_model_has_correct_field_types(self):
        """
        Test that the properties of the Coto Product Model are of the correct type
        """
        product = CotoProductModel.objects.get(name="Gouda Cheese")
        self.assertEqual(type(product.number), int)
        self.assertEqual(type(product.name), str)
        self.assertEqual(type(product.bulk_purchase_amount), int)
        self.assertEqual(type(product.bulk_purchase_measure), str)
        self.assertEqual(type(product.categories_path), str)
        self.assertEqual(type(product.image_url), str)
        self.assertEqual(type(product.link), str)
        self.assertEqual(type(product.created), datetime)
        self.assertEqual(type(product.last_modified), datetime)

class CotoProductPriceUpdateTestCase(TestCase):
    def setUp(self):
        CotoProductModel.objects.create(
            name = "Gouda Cheese",
            number = 123,
            bulk_purchase_amount = 2,
            bulk_purchase_measure = 'Kilograms',
            categories_path = 'frescos > queso > holandeses',
            image_url = 'https://www.google.com',
            link = 'https://www.google.com'
        ),
        CotoProductPriceUpdateModel.objects.create(
            product = CotoProductModel.objects.get(name="Gouda Cheese"),
            unit_price = 17.5,
            promo_required_amount = 2,
            promo_unit_price = 15.3,
            text_price_discount = '2x3',
            bulk_purchase_price = 32.4
        )

    def test_model_has_correct_field_types(self):
        """
        Test that the properties of the Coto Product Price Update Model are of the correct type
        """
        price_update = CotoProductPriceUpdateModel.objects.all()[0]
        self.assertEqual(type(price_update.product), CotoProductModel)
        self.assertEqual(type(price_update.unit_price), float)
        self.assertEqual(type(price_update.promo_required_amount), int)
        self.assertEqual(type(price_update.promo_unit_price), float)
        self.assertEqual(type(price_update.text_price_discount), str)
        self.assertEqual(type(price_update.bulk_purchase_price), float)
        self.assertEqual(type(price_update.update_date), datetime)





