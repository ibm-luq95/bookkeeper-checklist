# -*- coding: utf-8 -*-#
from django.urls import path, include
from users.views import (
    ManagerUsersListView,
    ManagerUsersCreateView,
    ManagerUsersArchiveListView,
    ManagerUsersChangeView,
    ManagerUsersDeleteView,
    ManagerUpdateUserPasswordView,
)

app_name = "manager"

urlpatterns = [
    path("", ManagerUsersListView.as_view(), name="list"),
    path("archive", ManagerUsersArchiveListView.as_view(), name="archive"),
    path("create", ManagerUsersCreateView.as_view(), name="create"),
    # path("update/<uuid:pk>", ManagerUsersChangeView.as_view(), name="update"),
    path("update/<uuid:pk>", ManagerUsersChangeView.as_view(), name="update"),
    path("delete/<uuid:pk>", ManagerUsersDeleteView.as_view(), name="delete"),
    path(
        "update_password/<uuid:pk>", ManagerUpdateUserPasswordView.as_view(), name="update-password"
    ),
]
