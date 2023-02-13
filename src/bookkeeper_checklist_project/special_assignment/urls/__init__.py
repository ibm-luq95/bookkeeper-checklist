# -*- coding: utf-8 -*-#
from django.urls import path, include
from special_assignment.views import (
    RequestedSpecialAssignmentsListView,
    SpecialAssignmentArchiveListView,
    SpecialAssignmentUpdateView,
    SpecialAssignmentListView,
    SpecialAssignmentCreateView,
    SpecialAssignmentDeleteView,
    SpecialAssignmentDetailsView,
)

app_name = "special_assignment"

urlpatterns = [
    path(
        "api/", include("special_assignment.urls.api"), name="special-assignment-api-urls"
    ),
    path("", SpecialAssignmentListView.as_view(), name="list"),
    path("requested", RequestedSpecialAssignmentsListView.as_view(), name="requested"),
    path("<uuid:pk>", SpecialAssignmentDetailsView.as_view(), name="details"),
    path("create", SpecialAssignmentCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", SpecialAssignmentUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", SpecialAssignmentDeleteView.as_view(), name="delete"),
    path("archive", SpecialAssignmentArchiveListView.as_view(), name="archive"),
    # path(
    #     "manager/",
    #     include("special_assignment.urls.manager"),
    #     name="special-assignment-manager-urls",
    # ),
]
