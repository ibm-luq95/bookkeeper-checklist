"""
Django settings for bookkeeper_checklist project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
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
    # "django.contrib.sites",
    "django_filters",
    "rest_framework",
    # "rest_framework.authtoken",
    "crispy_forms",
    "crispy_bulma",
    "betterforms",
    # "crispy_bootstrap5",
    "core.apps.CoreConfig",
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
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.cache.UpdateCacheMiddleware",  # new for the cache
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",  # new for the cache
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "core.errors.ExceptionMiddleware"
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

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "static"]

# STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_ROOT = (
    BASE_DIR
    / "/home/ibrahim/bookkeeper-checklist/src/bookkeeper_checklist_project/staticfiles"
)

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "/media/"

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
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
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

CRISPY_ALLOWED_TEMPLATE_PACKS = "bulma"

CRISPY_TEMPLATE_PACK = "bulma"

# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
#
# CRISPY_TEMPLATE_PACK = "bootstrap5"

AUTH_USER_MODEL = "users.CustomUser"

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
}
# check if cache enabled
if bool(os.environ.get("IS_CACHE_ENABLED")):
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
