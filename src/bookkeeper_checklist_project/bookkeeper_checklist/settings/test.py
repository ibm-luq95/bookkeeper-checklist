from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(", ")

DEBUG = ast.literal_eval(os.environ.get("DEBUG"))
