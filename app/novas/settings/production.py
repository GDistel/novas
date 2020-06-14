from .base import *

# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
# ]

#CORS_ORIGIN_WHITELIST = ()

DEBUG = False
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "novas",
        "USER": "novas",
        "PASSWORD": "novas",
        "HOST": "db",
        "PORT": "5432",
    }
}
