# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "company_services"

urlpatterns = [
    path("api/", include("company_services.urls.api"), name="company-services-api-urls"),
    path(
        "manager/",
        include("company_services.urls.manager"),
        name="company-services-manager-urls",
    ),
]
