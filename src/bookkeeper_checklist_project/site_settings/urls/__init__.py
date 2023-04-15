# -*- coding: utf-8 -*-#
from django.urls import path
from site_settings.views import SiteSettingsCreateView, ApplicationConfigurationsFormView

app_name = "site_settings"

urlpatterns = [
    path(
        "web-app",
        SiteSettingsCreateView.as_view(),
        name="web-app-settings",
    ),
    path(
        "app-configs",
        ApplicationConfigurationsFormView.as_view(),
        name="app-configs-settings",
    ),
]
