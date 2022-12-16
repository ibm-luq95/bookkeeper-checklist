# -*- coding: utf-8 -*-#
from django.db.models.signals import post_save

from core.cache import CacheHandler
from .models import SiteSettings
from core.constants.site_settings import WEB_APP_SETTINGS_KEY


def update_site_settings_cache(sender, instance, created, **kwargs):
    site_settings_object = instance
    slug = site_settings_object.slug
    if slug == "web-app":
        CacheHandler.delete_item(WEB_APP_SETTINGS_KEY)
        CacheHandler.set_item(WEB_APP_SETTINGS_KEY, site_settings_object)


post_save.connect(update_site_settings_cache, SiteSettings)
