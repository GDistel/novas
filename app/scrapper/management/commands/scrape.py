import time
import random
from django.core.management.base import BaseCommand
from scrapper.coto.routes import ROUTES, ROUTE_BATCHES
from scrapper.coto.utils import get_soup, get_detail_soup, scrap_product_data, scrap_detail_routes, get_all_detail_routes
from scrapper.models import CotoProductModel, CotoProductPriceUpdateModel

class Command(BaseCommand):
    help = "Collect Coto products"

    def add_arguments(self, parser):
        parser.add_argument(
            '--dev',
            action='store_true',
            help='Pokes detail views to start scrapping product data, for dev purpose'
        )
        parser.add_argument(
              '--batch',
               action = 'store',
               dest = 'batch',
               type = int,
               default = 1,
               help = 'Route batch number'
        )

    def handle(self, *args, **options):
        if options['dev']:
            soup = get_soup(ROUTES['almacen'])
            all_product_routes = scrap_detail_routes(soup)
            self.scrap_main_route(all_product_routes, 'almacen')
        else:
            if options['batch']:
                batch_number = options['batch']
                routes_to_scrap = ROUTE_BATCHES[str(batch_number)]
            else:
                routes_to_scrap = ROUTES
            for route_name, route_link in routes_to_scrap.items():
                print('\n', 'Processing data for category: ', route_name, '\n')
                all_product_routes = get_all_detail_routes(route_link, route_name)
                self.scrap_main_route(all_product_routes, route_name)

    def scrap_main_route(self, product_routes, route_name = ''):
        print('\n', f'Writing products to DB for category {route_name}', '\n')
        for prod_route in product_routes:
            detail_soup = get_detail_soup(prod_route)
            cleaned_product_data = scrap_product_data(detail_soup)
            product, created = CotoProductModel.objects.update_or_create(
                number = cleaned_product_data.get('number'),
                defaults = {
                    'name': cleaned_product_data.get('name'),
                    'bulk_purchase_amount': cleaned_product_data.get('bulk_purchase_amount'),
                    'bulk_purchase_measure': cleaned_product_data.get('bulk_purchase_measure'),
                    'categories_path': cleaned_product_data.get('categories_path'),
                    'image_url': cleaned_product_data.get('image_url'),
                    'link': prod_route
                }
            )

            CotoProductPriceUpdateModel.objects.create(
                product = product,
                unit_price = cleaned_product_data.get('unit_price'),
                promo_required_amount = cleaned_product_data.get('promo_required_amount'),
                promo_unit_price = cleaned_product_data.get('promo_unit_price'),
                text_price_discount = cleaned_product_data.get('text_price_discount'),
                bulk_purchase_price = cleaned_product_data.get('bulk_purchase_price'),
            )

            if created:
                print(f'\033[92m Product created: {product}')
            else:
                print(f'\033[92m Product updated: {product}')

            time.sleep(random.randint(1,5))

        return True
