# -*- coding: utf-8 -*-#
from django.urls import path, include
from company_services.views import (
    CompanyServicesUpdateView,
    CompanyServicesCreateView,
    CompanyServicesDeleteView,
    CompanyServicesListView,
)

app_name = "company_services"

urlpatterns = [
    path("api/", include("company_services.urls.api"), name="company-services-api-urls"),
    path("", CompanyServicesListView.as_view(), name="list"),
    path("create", CompanyServicesCreateView.as_view(), name="create"),
    path("delete/<uuid:pk>", CompanyServicesDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", CompanyServicesUpdateView.as_view(), name="update"),
]
