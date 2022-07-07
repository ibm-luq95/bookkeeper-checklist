import os

from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(", ")

DEBUG = bool(os.environ.get("DEBUG"))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "django.middleware.cache.UpdateCacheMiddleware", # new for the cache
    'django.middleware.common.CommonMiddleware',
    # "django.middleware.cache.FetchFromCacheMiddleware", # new for the cache
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Set Cache Configurations
# CACHE_MIDDLEWARE_ALIAS = 'bk_clst'  # which cache alias to use
# CACHE_MIDDLEWARE_SECONDS = '600'    # number of seconds to cache a page for (TTL)

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("DB_NAME"),
#         "USER": os.environ.get("DB_USER"),
#         "PASSWORD": os.environ.get("DB_PASSWORD"),
#         "HOST": os.environ.get("DB_HOST"),
#         "PORT": os.environ.get("DB_PORT"),
#     }
# }


# Cache Redis
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": f"redis://{os.environ.get('REDIS_HOST')}:{os.environ.get('REDIS_PORT')}",
#     }
# }
