# -*- coding: utf-8 -*-#
from django.urls import path
from bookkeeper.views import (
    SpecialAssignmentsListView,
    SpecialAssignmentDetailsView,
    SpecialAssignmentCreateView,
    RequestedSpecialAssignmentsListView,
    SpecialAssignmentUpdateView,
)

app_name = "special_assignment"

urlpatterns = [
    path("", SpecialAssignmentsListView.as_view(), name="list"),
    path("requested", RequestedSpecialAssignmentsListView.as_view(), name="requested"),
    path("create", SpecialAssignmentCreateView.as_view(), name="create"),
    path("<uuid:pk>", SpecialAssignmentDetailsView.as_view(), name="details"),
    path("update/<uuid:pk>", SpecialAssignmentUpdateView.as_view(), name="update"),
]
