import os

from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(", ")

DEBUG = bool(os.environ.get("DEBUG"))

INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar",
    "django_extensions",
]

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
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
        "OPTIONS": {
            # "read_default_file": "/opt/lampp/etc/my.cnf",
            "init_command": "SET default_storage_engine=INNODB",
        },
    }
}

# Set Cache Configurations
CACHES = {
    "default": {
        "BACKEND": os.environ.get("CACHE_BACKEND_ENGINE"),
        "LOCATION": f"redis://:{os.environ.get('REDIS_PASSWORD')}@{os.environ.get('REDIS_HOST')}:{os.environ.get('REDIS_PORT')}",
        "TIMEOUT": None,
    }
}

# Djagno Debug Toolbar
INTERNAL_IPS = os.environ.get("INTERNAL_IPS").split(", ")
DISABLE_PANELS = {}

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

SHOW_COLLAPSED = True


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

if DEBUG:
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
