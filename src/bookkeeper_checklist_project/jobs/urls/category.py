# -*- coding: utf-8 -*-#
from django.urls import path

from jobs.views import (
    JobCategoryListView,
    JobCategoryCreateView,
    JobCategoryDeleteView,
    JobCategoryUpdateView,
)

app_name = "category"

urlpatterns = [
    path("", JobCategoryListView.as_view(), name="list"),
    path("create", JobCategoryCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", JobCategoryUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", JobCategoryDeleteView.as_view(), name="delete"),
]
