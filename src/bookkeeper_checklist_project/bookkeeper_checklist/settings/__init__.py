
from decouple import config

from core.utils import get_formatted_logger

# from dotenv import load_dotenv

logger = get_formatted_logger()

### [ONLY FOR DEPLOYMENT] ###
# dotenv_path = os.path.join("/home/ibrahim/bookkeeper-checklist/src", ".env")
# load_dotenv(dotenv_path=dotenv_path)  # load all environment variables from .env.
### [ONLY FOR DEPLOYMENT] ###
# load_dotenv()
# from pprint import pprint
# pprint(os.environ)
# pprint()
environment = config("STAGE_ENVIRONMENT", cast=str)
# environment = os.environ.get("STAGE_ENVIRONMENT")
logger.info(f" Environment is: ({environment})")

if environment == "DEV":
    from .dev import *
elif environment == "PRODUCTION":
    from .production import *
elif environment == "TEST":
    from .test import *
elif environment == "LOCAL":
    from .local import *
elif environment == "STAGE":
    from .stage import *
