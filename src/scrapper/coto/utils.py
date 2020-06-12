import re
import time
import random
import requests
import csv
from bs4 import BeautifulSoup
import scrapper.coto.cleaners as clean
from scrapper.coto.routes import DETAIL_ROUTE_PATTERN, BASE_URL

def get_soup(route):
    http = requests.Session()
    http.headers.update({
        'User-Agent': 'Googlebot'
    })
    keep_trying = True
    while keep_trying:
        try:
            page = http.get(route)
            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'html.parser')
                keep_trying = False
        except:
            print('\n', 'Exception ocurred. Will try again in 1 minute...', '\n')
            time.sleep(60)

    return soup

def get_detail_soup(route):
    soup = get_soup(route)
    bread_crumbs_soup = soup.select_one('div#atg_store_breadcrumbs')
    bulk_data_soup = soup.select_one('span.unit')
    product_soup = soup.select_one('div.atg_store_productSingleSkuWide')
    return bread_crumbs_soup, product_soup, bulk_data_soup

def get_value_or_none(soup, selector, mode = 'find', attr = 'innerHTML'):
    if mode == 'find':
        elem = soup.find(class_ = selector)
        if elem is None:
            return
        elem = elem.get_text()
    elif mode == 'select_one':
        elem = soup.select_one(selector)
        if elem is None:
            return
        elem = elem.get(attr)
    elif mode == 'select':
        elem = soup.select(selector)
        if elem is None:
            return
        elem = elem
    
    return elem


def scrap_product_data(detail_soup):
    '''
    Extract the product information from the markup of Coto's product detail page.
    Return a dictionary with the cleaned scrapped data
    '''
    bread_crumbs_soup, product_soup, bulk_data_soup = detail_soup

    unit_price = get_value_or_none(product_soup, 'atg_store_newPrice')
    unit_price = clean.unit_price(unit_price)

    name_number = get_value_or_none(product_soup, 'product_page')
    name, number = clean.name_number(name_number)

    promo_required_amount = get_value_or_none(product_soup, 'desc-llevandoN')
    promo_required_amount = clean.promo_required_amount(promo_required_amount)

    promo_unit_price = get_value_or_none(product_soup, 'price_discount')
    promo_unit_price = clean.promo_unit_price(promo_unit_price)

    text_price_discount = get_value_or_none(product_soup, 'text_price_discount')
    text_price_discount = clean.text_price_discount(text_price_discount)

    bulk_purchase_data = bulk_data_soup.get_text()
    bulk_purchase_amount, bulk_purchase_measure, bulk_purchase_price = clean.bulk_purchase(bulk_purchase_data)

    categories_path_data = get_value_or_none(bread_crumbs_soup, 'a > p', mode = 'select')
    categories_path = clean.categories_path(categories_path_data)
    
    image_url = get_value_or_none(product_soup, 'a.gall-item > img', 'select_one', 'src')

    product = {
        'name': name,
        'number': int(number),
        'unit_price': None if unit_price is None else float(unit_price),
        'promo_required_amount': None if promo_required_amount is None else int(promo_required_amount),
        'promo_unit_price': None if promo_unit_price is None else float(promo_unit_price),
        'text_price_discount': text_price_discount,
        'bulk_purchase_amount': None if bulk_purchase_amount is None else int(bulk_purchase_amount),
        'bulk_purchase_measure': bulk_purchase_measure,
        'bulk_purchase_price': None if bulk_purchase_price is None else float(bulk_purchase_price),
        'categories_path': categories_path,
        'image_url': image_url
    }

    return product

def scrap_detail_routes(soup):
    '''
    Takes a bs4 soup and returns all product detail routes found for a Coto product category.
    It works on the visible list-view)
    '''
    detail_routes = []
    page_products = soup.findAll('a', href=DETAIL_ROUTE_PATTERN)
    for prod in page_products:
        detail_route = prod['href']
        detail_routes.append(f'{BASE_URL}{detail_route}')

    return detail_routes

def get_next_page_route(soup, current_page_number):
    '''
    Returns the route of the next list-view page.
    Otherwise it returns None
    '''
    full_route = None
    partial_route = None
    paginator = soup.select('ul#atg_store_pagination > li > a')
    for page_link in paginator:
        content = page_link.get_text()
        if (content == 'Ant') or (content == 'Sig'): #Anterior, siguiente
            continue
        if int(content) == (current_page_number + 1):
            partial_route = page_link['href']
            break

    if partial_route:
        full_route = f'{BASE_URL}{partial_route}'

    return full_route
    

def get_all_detail_routes(category_route, route_name):
    '''
    Scraps each product detail-page link. Returns an array with all these routes.
    '''
    all_detail_routes = []
    list_view_route = category_route
    page_number = 1
    with open(f'scrapper/coto/.test_data/{route_name}_detail_routes.csv', mode='w') as detail_routes:
        routes_file = csv.writer(detail_routes, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        routes_file.writerow(['List-view route'])
        while page_number > 0:
            print('Scraping routes in page', page_number, f'of {route_name}')
            routes_file.writerow([list_view_route])
            soup = get_soup(list_view_route)
            page_detail_routes = scrap_detail_routes(soup)
            all_detail_routes.extend(page_detail_routes)
            next_list_view_route = get_next_page_route(soup, page_number)
            if type(next_list_view_route) == str:
                list_view_route = next_list_view_route
                page_number += 1
                time.sleep(random.randint(1,6))
            else:
                page_number = 0

    return all_detail_routes

def use_production_route(route):
    return route.replace(CACHED_BASE_URL, BASE_URL)


