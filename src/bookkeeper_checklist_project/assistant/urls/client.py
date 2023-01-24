# -*- coding: utf-8 -*-#
from django.urls import path
from assistant.views import (
    ClientListView,
    ClientCreateView,
    ClientDetailsView,
    ClientUpdateView,
)

app_name = "client"

urlpatterns = [
    path("", ClientListView.as_view(), name="list"),
    path("create", ClientCreateView.as_view(), name="create"),
    path("<uuid:pk>", ClientDetailsView.as_view(), name="details"),
    path("update/<uuid:pk>", ClientUpdateView.as_view(), name="update"),
]
