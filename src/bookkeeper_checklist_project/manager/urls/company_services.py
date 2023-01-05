# -*- coding: utf-8 -*-#
from django.urls import path
from manager.views import (
    CompanyServicesListView,
    CompanyServicesDeleteView,
    CompanyServicesCreateView,
    CompanyServicesUpdateView,
)

app_name = "company_services"

urlpatterns = [
    path("", CompanyServicesListView.as_view(), name="list"),
    path("create", CompanyServicesCreateView.as_view(), name="create"),
    # path("<uuid:pk>", ClientDetailView.as_view(), name="details"),
    path("update/<uuid:pk>", CompanyServicesUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", CompanyServicesDeleteView.as_view(), name="delete"),
]
