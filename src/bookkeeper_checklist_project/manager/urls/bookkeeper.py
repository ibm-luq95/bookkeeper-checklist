from django.urls import path

from manager.views import (
    BookkeepersListView,
    BookkeepersDetailsView,
    BookkeeperDeleteView,
    BookkeeperCreateView,
    BookkeeperUpdateView,
)

app_name = "bookkeeper"

urlpatterns = [
    # path("api/", include("manager.urls.api"), name="manager-bookkeeper-api-urls"),
    path("", BookkeepersListView.as_view(), name="list"),
    path("create", BookkeeperCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", BookkeeperUpdateView.as_view(), name="update"),
    path("<uuid:pk>", BookkeepersDetailsView.as_view(), name="details"),
    path("delete/<uuid:pk>", BookkeeperDeleteView.as_view(), name="delete"),
]
