# -*- coding: utf-8 -*-#
from django.urls import path
from manager.views import (
    ManagerListView,
    ManagerCreateView,
    ManagerDeleteView,
    ManagerArchiveView,
    ManagerUpdateView,
)

app_name = "manager"


urlpatterns = [
    # path("api/", include("manager.urls.api"), name="manager-bookkeeper-api-urls"),
    path("", ManagerListView.as_view(), name="list"),
    path("archive", ManagerArchiveView.as_view(), name="archive"),
    path("create", ManagerCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ManagerUpdateView.as_view(), name="update"),
    # path("<uuid:pk>", BookkeepersDetailsView.as_view(), name="details"),
    path("delete/<uuid:pk>", ManagerDeleteView.as_view(), name="delete"),
]
