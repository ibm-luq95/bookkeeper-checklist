"""
Django settings for bookkeeper_checklist project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import ast
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent  # default
BASE_DIR = (
    Path(__file__).resolve().parent.parent.parent
)  # custom BASE_DIR to match the project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # "django_extensions",
    "maintenance_mode",
    # "django.contrib.sites",
    "django_filters",
    "rest_framework",
    # "rest_framework.authtoken",
    "crispy_forms",
    "crispy_bulma",
    "betterforms",
    "core.apps.CoreConfig",
    "site_settings.apps.SiteSettingsConfig",
    "users.apps.UsersConfig",
    "manager.apps.ManagerConfig",
    "assistant.apps.AssistantConfig",
    "bank_account.apps.BankAccountConfig",
    "bookkeeper.apps.BookkeeperConfig",
    "important_contact.apps.ImportantContactConfig",
    "documents.apps.DocumentsConfig",
    "client_account.apps.ClientAccountConfig",
    "client.apps.ClientConfig",
    "company_services.apps.CompanyServicesConfig",
    "notes.apps.NotesConfig",
    "jobs.apps.JobsConfig",
    "task.apps.TaskConfig",
    "special_assignment.apps.SpecialAssignmentConfig",
]

MIDDLEWARE = [
    # "django.middleware.cache.UpdateCacheMiddleware",  # new for the cache
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_session_timeout.middleware.SessionTimeoutMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "bookkeeper.middleware.BookkeeperMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",  # new for the cache
]

ROOT_URLCONF = "bookkeeper_checklist.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "site_settings.context_processors.return_all_context",
                "maintenance_mode.context_processors.maintenance_mode",
            ],
        },
    },
]

WSGI_APPLICATION = "bookkeeper_checklist.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
WHITENOISE_MANIFEST_STRICT = ast.literal_eval(os.environ.get("WHITENOISE_MANIFEST_STRICT"))

# STATIC_ROOT = (
#     BASE_DIR
#     / "/home/ibrahim/bookkeeper-checklist/src/bookkeeper_checklist_project/staticfiles"
# )
# STATIC_ROOT = (
#     BASE_DIR
#     / "staticfiles"
# )

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Use new password Scrypt algorithm
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Enabling password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 7,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

MESSAGE_TAGS = {
    messages.DEBUG: "is-link",
    messages.INFO: "is-info",
    messages.SUCCESS: "is-success",
    messages.WARNING: "is-warning",
    messages.ERROR: "is-danger",
}

LOGIN_REDIRECT_URL = ""
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "users:login"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bulma"

CRISPY_TEMPLATE_PACK = "bulma"

AUTH_USER_MODEL = "users.CustomUser"

SESSION_COOKIE_AGE = int(os.environ.get("SESSION_COOKIE_AGE"))

REST_FRAMEWORK = {
    # "EXCEPTION_HANDLER": "core.errors.api_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        # "rest_framework.parsers.FormParser",
    ],
    "DATETIME_FORMAT": "%Y-%m-%d",
}

# if True the maintenance-mode will be activated
# MAINTENANCE_MODE = False
# by default, a file named "maintenance_mode_state.txt" will be created in the settings.py directory
# you can customize the state file path in case the default one is not writable
MAINTENANCE_MODE_STATE_FILE_PATH = BASE_DIR / "maintenance_mode_state.txt"
# the template that will be shown by the maintenance-mode page
MAINTENANCE_MODE_TEMPLATE = "maintenance/503.html"

# the HTTP status code to send
# MAINTENANCE_MODE_STATUS_CODE = 404

# list of urls that will not be affected by the maintenance-mode
# urls will be used to compile regular expressions objects
MAINTENANCE_MODE_IGNORE_URLS = (r"^/manager", r"/logout", r"/")

# if True admin site will not be affected by the maintenance-mode page
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True

# if True the superuser will not see the maintenance-mode page
MAINTENANCE_MODE_IGNORE_SUPERUSER = False

# Session configs
SESSION_EXPIRE_SECONDS = int(os.environ.get("SESSION_EXPIRE_SECONDS"))  # 1 hour
SESSION_EXPIRE_AT_BROWSER_CLOSE = ast.literal_eval(
    os.environ.get("SESSION_EXPIRE_AT_BROWSER_CLOSE")
)  # Invalid session
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = ast.literal_eval(
    os.environ.get("SESSION_EXPIRE_AFTER_LAST_ACTIVITY")
)

# SESSION_TIMEOUT_REDIRECT = "/"
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 60  # group by minute

# LOGGING = {
#     "version": 1,
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             # "filename": BASE_DIR / "debug.log",
#         },
#     },
#     "loggers": {
#         "werkzeug": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#     },
# }
LOGGING = {
    "version": 1,
    # The version number of our log
    "disable_existing_loggers": False,
    # django uses some of its own loggers for internal operations. In case you want to disable them just replace the False above with true.
    # A handler for WARNING. It is basically writing the WARNING messages into a file called WARNING.log
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "errors.log",
        },
    },
    # A logger for WARNING which has a handler called 'file'. A logger can have multiple handler
    "loggers": {
        # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        "": {
            "handlers": [
                "file"
            ],  # notice how file variable is called in handler which has been defined above
            "level": "ERROR",
            "propagate": True,
        },

    },
}
# check if cache enabled
if ast.literal_eval(os.environ.get("IS_CACHE_ENABLED")) is True:
    CACHE_MIDDLEWARE_ALIAS = os.environ.get(
        "CACHE_MIDDLEWARE_ALIAS"
    )  # which cache alias to use
    CACHE_MIDDLEWARE_SECONDS = int(
        os.environ.get("CACHE_MIDDLEWARE_SECONDS")
    )  # number of seconds to cache a page for (TTL)

    CACHE_MIDDLEWARE_KEY_PREFIX = os.environ.get(
        "CACHE_MIDDLEWARE_KEY_PREFIX"
    )  # should be used if the cache is shared across multiple sites that
    # use the
    # same
    # Django instance
