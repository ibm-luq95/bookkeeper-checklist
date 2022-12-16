# -*- coding: utf-8 -*-#
from django.urls import path
from site_settings.views import SiteSettingsCreateView

app_name = "site_settings"

urlpatterns = [
    path(
        "web-app",
        SiteSettingsCreateView.as_view(),
        name="web-app-settings",
    ),
]
