# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path(
        "manager/",
        include("company_services.urls.api.manager"),
        name="manager-company-services-api-urls",
    )
]
