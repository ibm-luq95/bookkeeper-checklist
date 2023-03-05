# -*- coding: utf-8 -*-#
from django.urls import path, include
from client.views import (
    ClientListView,
    ClientCreateView,
    ClientArchiveListView,
    ClientUpdateView,
    ClientDetailsView,
    ClientDetailsOverviewRedirectView,
    ClientDeleteView,
)

app_name = "client"

urlpatterns = [
    path("category/", include("client.urls.category"), name="client-category-urls"),
    path("", ClientListView.as_view(), name="list"),
    path("archive/", ClientArchiveListView.as_view(), name="archive"),
    path("create", ClientCreateView.as_view(), name="create"),
    path(
        "<uuid:pk>/",
        include(
            (
                [
                    path(
                        "",
                        ClientDetailsOverviewRedirectView.as_view(),
                        name="default",
                    ),
                    path("overview", ClientDetailsView.as_view(), name="overview"),
                    path("contacts", ClientDetailsView.as_view(), name="contacts"),
                    path("documents", ClientDetailsView.as_view(), name="documents"),
                    path(
                        "assignments",
                        ClientDetailsView.as_view(),
                        name="assignments",
                    ),
                    path("services", ClientDetailsView.as_view(), name="services"),
                    path("tasks", ClientDetailsView.as_view(), name="tasks"),
                    path("jobs", ClientDetailsView.as_view(), name="jobs"),
                    path("notes", ClientDetailsView.as_view(), name="notes"),
                ],
                "details",
            )
        ),
        name="details",
    ),
    path("update/<uuid:pk>", ClientUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ClientDeleteView.as_view(), name="delete"),
    # path("manager/", include("client.urls.manager"), name="client-manager-urls"),
    # path("assistant/", include("client.urls.assistant"), name="client-assistant-urls"),
    # path(
    #     "bookkeeper/",
    #     include("client.urls.bookkeeper"),
    #     name="client-bookkeeper-urls",
    # ),
]
