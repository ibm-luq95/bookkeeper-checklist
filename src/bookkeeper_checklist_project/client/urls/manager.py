# -*- coding: utf-8 -*-#
from django.urls import path, include

from client.views import (
    ManagerClientListView,
    ManagerClientCreateView,
    ManagerClientDetailsView,
    ManagerClientUpdateView,
    ManagerClientDeleteView,
    ManagerClientDetailsOverviewRedirectView,
    ManagerClientArchiveListView
)

app_name = "manager"

urlpatterns = [
    path("create/", ManagerClientCreateView.as_view(), name="create"),
    path("list/", ManagerClientListView.as_view(), name="list"),
    path("archive/", ManagerClientArchiveListView.as_view(), name="archive"),
    path(
        "<uuid:pk>/",
        include(
            (
                [
                    path(
                        "",
                        ManagerClientDetailsOverviewRedirectView.as_view(),
                        name="default",
                    ),
                    path("overview", ManagerClientDetailsView.as_view(), name="overview"),
                    path("contacts", ManagerClientDetailsView.as_view(), name="contacts"),
                    path("documents", ManagerClientDetailsView.as_view(), name="documents"),
                    path("assignments", ManagerClientDetailsView.as_view(), name="assignments"),
                    path("services", ManagerClientDetailsView.as_view(), name="services"),
                    path("tasks", ManagerClientDetailsView.as_view(), name="tasks"),
                    path("jobs", ManagerClientDetailsView.as_view(), name="jobs"),
                    path("notes", ManagerClientDetailsView.as_view(), name="notes"),
                ],
                "details",
            )
        ),
        name="details",
    ),
    path("update/<uuid:pk>", ManagerClientUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ManagerClientDeleteView.as_view(), name="delete"),
]
