# -*- coding: utf-8 -*-#
from django.urls import path, include
from client.views import (
    ClientCategoryListView,
    ClientCategoryCreateView,
    ClientCategoryUpdateView,
    ClientCategoryDeleteView,
)

app_name = "category"

urlpatterns = [
    path("", ClientCategoryListView.as_view(), name="list"),
    path("create", ClientCategoryCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ClientCategoryUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ClientCategoryDeleteView.as_view(), name="delete"),
]
