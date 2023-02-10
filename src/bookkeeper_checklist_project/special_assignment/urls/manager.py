# -*- coding: utf-8 -*-#
from django.urls import path
from special_assignment.views import (
    ManagerSpecialAssignmentUpdateView,
    ManagerSpecialAssignmentDetailsView,
    ManagerSpecialAssignmentDeleteView,
    ManagerSpecialAssignmentCreateView,
    ManagerRequestedSpecialAssignmentsListView,
    ManagerSpecialAssignmentListView,
    ManagerSpecialAssignmentArchiveListView,
)

app_name = "manager"

urlpatterns = [
    path("", ManagerSpecialAssignmentListView.as_view(), name="list"),
    path(
        "requested", ManagerRequestedSpecialAssignmentsListView.as_view(), name="requested"
    ),
    path("<uuid:pk>", ManagerSpecialAssignmentDetailsView.as_view(), name="details"),
    path("create", ManagerSpecialAssignmentCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ManagerSpecialAssignmentUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ManagerSpecialAssignmentDeleteView.as_view(), name="delete"),
    path("archive", ManagerSpecialAssignmentArchiveListView.as_view(), name="archive"),
]
