# -*- coding: utf-8 -*-#
from django.urls import path

from company_services.views import CreateCompanyServiceManagerApiView

app_name = "manager"

urlpatterns = [
    path(
        "create",
        CreateCompanyServiceManagerApiView.as_view(),
        name="create",
    ),
]
