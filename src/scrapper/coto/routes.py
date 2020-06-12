import re

BASE_URL = 'https://www.cotodigital3.com.ar'

DETAIL_ROUTE_PATTERN = re.compile('^/sitios/cdigi/producto')

ROUTES = {
    'almacen': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-almac%C3%A9n/_/N-8pub5z',
    'bebidas': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-bebidas/_/N-1c1jy9y',
    'frescos': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-frescos/_/N-1ewuqo6',
    'congelados': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-congelados/_/N-1xgbihs',
    'limpieza': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-limpieza/_/N-nityfw',
    'perfumeria': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-perfumer%C3%ADa/_/N-cblpjz',
    'electro': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-electro/_/N-1ngpk59',
    'textil': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-textil/_/N-l8joi7',
    'hogar': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-hogar/_/N-qa34ar',
    'aire_libre': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-aire-libre/_/N-w7wnle',
}

ROUTES_BATCH_1 = {
    'almacen': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-almac%C3%A9n/_/N-8pub5z',
    'bebidas': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-bebidas/_/N-1c1jy9y',
    'perfumeria': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-perfumer%C3%ADa/_/N-cblpjz'
}

ROUTES_BATCH_2 = {
    'frescos': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-frescos/_/N-1ewuqo6',
    'congelados': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-congelados/_/N-1xgbihs',
    'limpieza': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-limpieza/_/N-nityfw',
    'electro': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-electro/_/N-1ngpk59',
    'textil': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-textil/_/N-l8joi7',
    'aire_libre': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-aire-libre/_/N-w7wnle',
}

ROUTES_BATCH_3 = {
    'hogar': 'https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-hogar/_/N-qa34ar',
}
