import logging
import os

from dotenv import load_dotenv

log = logging.getLogger(__name__)

load_dotenv()  # load all environment variables from .env.

environment = os.environ.get("STAGE_ENVIRONMENT")
log.info(f" Environment is: ({environment})")
if environment == "DEV":
    from .dev import *
elif environment == "PRODUCTION":
    from .production import *
elif environment == "TEST":
    from .test import *
elif environment == "LOCAL":
    from .local import *
