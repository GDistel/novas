from .base import *
import dj_database_url

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'novas-server.herokuapp.com']

CORS_ORIGIN_ALLOW_ALL = True

DEBUG = False
#SECURE_SSL_REDIRECT = True
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

DATABASE_URL = os.environ.get("DATABASE_URL")
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)
if db_from_env:
    DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
