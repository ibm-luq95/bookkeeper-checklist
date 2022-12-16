# -*- coding: utf-8 -*-#
from typing import Union

from core.cache import CacheHandler
from core.utils import debugging_print
from site_settings.models import SiteSettings
from core.constants.site_settings import WEB_APP_SETTINGS_KEY


def get_web_app_settings(request) -> Union[SiteSettings, None]:
    if request.user.is_authenticated:
        site_settings = SiteSettings.objects.select_related().filter(slug="web-app").first()
        if site_settings:
            return CacheHandler.get_item(WEB_APP_SETTINGS_KEY)


def return_all_context(request):
    return {"get_web_app_settings": get_web_app_settings(request)}
