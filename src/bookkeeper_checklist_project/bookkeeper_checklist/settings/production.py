from .base import *

# ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=str).split(",")
DEBUG = config("DEBUG", cast=bool)

# SITE_NAME = "app.beachwoodfinancial.com"

# Database configurations
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", cast=str),
        "NAME": config("DB_NAME", cast=str),
        "USER": config("DB_USER", cast=str),
        "PASSWORD": config("DB_PASSWORD", cast=str),
        "HOST": config("DB_HOST", cast=str),
        "PORT": config("DB_PORT", cast=str),
        "OPTIONS": {
            "client_encoding": config("DB_CLIENT_ENCODING", cast=str),
        },
    }
}
# Cache configurations
CACHES = {
    "default": {
        "BACKEND": config("CACHE_BACKEND_ENGINE", cast=str),
        "LOCATION": f"redis://{config('REDIS_USER', cast=str)}:{config('REDIS_PASSWORD', cast=str)}"
        f"@{config('REDIS_HOST', cast=str)}:{config('REDIS_PORT', cast=str)}",
        "TIMEOUT": None,
    }
}

# ENCRYPT_KEY
ENCRYPT_KEY = bytes(config("ENCRYPT_KEY", cast=str), "ascii")

# Django production deployment settings
CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", cast=bool)
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", cast=bool)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool)
SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", cast=bool)
SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", cast=bool)
USE_X_FORWARDED_HOST = config("USE_X_FORWARDED_HOST", cast=bool)
