import os

from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(", ")

DEBUG = bool(os.environ.get("DEBUG"))

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",  # new for the cache
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",  # new for the cache
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Database configurations
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}

# Set Cache Configurations
# CACHE_MIDDLEWARE_ALIAS = os.environ.get("CACHE_MIDDLEWARE_ALIAS")  # which cache alias to use
# CACHE_MIDDLEWARE_SECONDS = os.environ.get(
#     "CACHE_MIDDLEWARE_SECONDS"
# )  # number of seconds to cache a page for (TTL)

# Cache Redis
CACHES = {
    "default": {
        "BACKEND": os.environ.get("CACHE_BACKEND_ENGINE"),
        "LOCATION": f"redis://{os.environ.get('REDIS_HOST')}:{os.environ.get('REDIS_PORT')}",
    }
}
