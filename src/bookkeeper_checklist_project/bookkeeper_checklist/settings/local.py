from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(", ")

DEBUG = config("DEBUG", cast=bool)
