# -*- coding: utf-8 -*-#
from django.urls import path, include
from company_services.views import (
    ManagerCompanyServicesUpdateView,
    ManagerCompanyServicesDeleteView,
    ManagerCompanyServicesCreateView,
    ManagerCompanyServicesListView,
)

app_name = "manager"

urlpatterns = [
    path("", ManagerCompanyServicesListView.as_view(), name="list"),
    path("create", ManagerCompanyServicesCreateView.as_view(), name="create"),
    path("delete/<uuid:pk>", ManagerCompanyServicesDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", ManagerCompanyServicesUpdateView.as_view(), name="update"),
]
