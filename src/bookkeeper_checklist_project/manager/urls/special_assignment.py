# -*- coding: utf-8 -*-#
from django.urls import path
from manager.views import (
    SpecialAssignmentListView,
    SpecialAssignmentCreateView,
    SpecialAssignmentUpdateView,
    SpecialAssignmentDeleteView,
    SpecialAssignmentDetailsView
)

app_name = "special_assignment"

urlpatterns = [
    path("", SpecialAssignmentListView.as_view(), name="list"),
    path("<uuid:pk>", SpecialAssignmentDetailsView.as_view(), name="details"),
    path("create", SpecialAssignmentCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", SpecialAssignmentUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", SpecialAssignmentDeleteView.as_view(), name="delete"),
]
