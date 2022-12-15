from core.admin import BaseAdminModelMixin
from django.contrib import admin

from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(BaseAdminModelMixin):
    pass
