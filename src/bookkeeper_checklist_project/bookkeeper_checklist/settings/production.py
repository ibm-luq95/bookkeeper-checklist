from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(", ")
DEBUG = ast.literal_eval(os.environ.get("DEBUG"))

# Database configurations
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
        "OPTIONS": {
            "client_encoding": os.environ.get("DB_CLIENT_ENCODING"),
        },
    }
}
# Cache configurations
CACHES = {
    "default": {
        "BACKEND": os.environ.get("CACHE_BACKEND_ENGINE"),
        "LOCATION": f"redis://{os.environ.get('REDIS_USER')}:{os.environ.get('REDIS_PASSWORD')}"
        f"@{os.environ.get('REDIS_HOST')}:{os.environ.get('REDIS_PORT')}",
        "TIMEOUT": None,
    }
}

# ENCRYPT_KEY
ENCRYPT_KEY = bytes(os.environ.get("ENCRYPT_KEY"), "ascii")

# Django production deployment settings
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
USE_X_FORWARDED_HOST = True
