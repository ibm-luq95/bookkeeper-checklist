# -*- coding: utf-8 -*-#
from django.urls import path, include
from assistant.views import (
    ClientListView,
    ClientCreateView,
    ClientDetailsView,
    ClientUpdateView,
    ClientDetailsJobsView,
    ClientDetailsTasksView,
    ClientDetailsSpecialAssignmentsView,
    ClientDetailsDocumentsView,
    ClientDetailsNotesView,
    ClientDetailsAccountsAndServicesView,
    ClientDetailsOverviewRedirectView,
    ClientDetailsContactsView,
)

app_name = "client"

urlpatterns = [
    path("", ClientListView.as_view(), name="list"),
    path("create", ClientCreateView.as_view(), name="create"),
    path(
        "<uuid:pk>/",
        include(
            [
                path(
                    "",
                    ClientDetailsOverviewRedirectView.as_view(),
                    name="overview-redirect",
                ),
                path("overview", ClientDetailsView.as_view(), name="overview"),
                path("contacts", ClientDetailsContactsView.as_view(), name="contacts"),
                path("jobs", ClientDetailsJobsView.as_view(), name="jobs"),
                path("tasks", ClientDetailsTasksView.as_view(), name="tasks"),
                path("documents", ClientDetailsDocumentsView.as_view(), name="documents"),
                path("notes", ClientDetailsNotesView.as_view(), name="notes"),
                path(
                    "services",
                    ClientDetailsAccountsAndServicesView.as_view(),
                    name="services",
                ),
                path(
                    "assignments",
                    ClientDetailsSpecialAssignmentsView.as_view(),
                    name="assignments",
                ),
            ]
        ),
        name="details",
    ),
    path("update/<uuid:pk>", ClientUpdateView.as_view(), name="update"),
]
