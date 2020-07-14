import re

def clean_string(string):
    '''
    Removes new lines and tabbed spacing.
    '''
    if type(string) is not str:
        return
    words_list = re.findall(r'([\S]+)', string)
    separator = ' '
    return separator.join(words_list)

def unit_price(raw_unit_price):
    '''
    Returns the unit price of the product ('Precio de contado') as float.
    The scrapped data originally comes as 'PRECIO CONTADO $145.00'
    '''
    if raw_unit_price is None:
        return
    split_data = clean_string(raw_unit_price).split('$')
    unit_price_string = split_data[1] 
    return float(unit_price_string)

def capture_product_number(product_name):
    '''
    See name_number doc string
    '''
    result = re.findall(r'\((\d+)\)', product_name)
    if result is None:
        return ''
    return result[0]

def name_number(raw_name_number):
    '''
    Returns a tuple with the extracted product name and number.
    The scrapped data comes as 'Product_name (product_number)'
    '''
    if raw_name_number is None:
        return
    name_number_string = clean_string(raw_name_number)
    number = capture_product_number(name_number_string)
    name = name_number_string.split(f' ({number}')[0]
    return name, number

def promo_required_amount(raw_promo_required_amount):
    '''
    Returns the promotion required amount from a string that usually comes
    in the form of 'Llevando n' (where 'n' is an integer). If you take n,
    the promotion applies.
    '''
    if raw_promo_required_amount is None:
        return
    promo_required_amount_string = clean_string(raw_promo_required_amount)
    promo_required_amount_string = promo_required_amount_string.split(' ')[1]
    return int(promo_required_amount_string)

def promo_unit_price(raw_promo_unit_price):
    '''
    Returns the promotional unit price. The scrapped data comes as: '$8.63c/u'
    or '$8.63' depending on whether a promotional required amount applies or not.
    '''
    if raw_promo_unit_price is None:
        return
    capture = re.findall(r'(\d+\.{1}\d+)',raw_promo_unit_price)
    promo_unit_price_string = capture[0]
    return float(promo_unit_price_string)

def text_price_discount(raw_text_price_discount):
    '''
    Returns the cleaned label for the discount. E.g. '80% 2da' or '6x5'.
    It tells what is the advantage of the discount
    '''
    if raw_text_price_discount is None:
        return
    text_price_discount_string = clean_string(raw_text_price_discount)
    return text_price_discount_string

def bulk_purchase(raw_bulk_purchase):
    '''
    Returns a tuple with the capture information for bulk pricing.
    For example: (1, 'Liter', 15.83).
    The raw form of the input is usually something lik "Precio por 1 Litro : $4.28"
    '''
    if raw_bulk_purchase is None:
        return None, None, None
    bulk_purchase_string = clean_string(raw_bulk_purchase)
    bulk_purchase_capture_pattern = re.compile('Precio por (\d+) (.+)\s?: \$(\d+\.\d+)')
    captures = re.findall(bulk_purchase_capture_pattern, bulk_purchase_string)
    if captures:
        amount, measure, price = captures[0]
        return int(amount), measure, float(price)
    else:
        print('No captures for this product')
        return None, None, None
    
def categories_path(categories_path_list):
    '''
    Takes a list of soup items, one for each node of the breadcrumbs.
    Returns a string of shape: category_1 > category_2 > category_3
    '''
    cleaned_list = []
    for path_item in categories_path_list:
        cleaned_item = clean_string(path_item.get_text())
        if '>' in cleaned_item:
            cleaned_item = cleaned_item.replace('>', '')
            cleaned_item = clean_string(cleaned_item)
        cleaned_list.append(cleaned_item)

    if 'Inicio' in cleaned_list:
        cleaned_list.remove('Inicio')

    return ' > '.join(cleaned_list)
