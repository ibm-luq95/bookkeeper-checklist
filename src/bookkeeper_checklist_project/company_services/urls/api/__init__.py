# -*- coding: utf-8 -*-#
from django.urls import path, include
from company_services.views.api import CreateCompanyServiceApiView

app_name = "api"

urlpatterns = [
    path("create", CreateCompanyServiceApiView.as_view(), name="create"),
]
