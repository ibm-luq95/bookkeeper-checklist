from django.urls import path, include
from manager.views import (
    BookkeepersListView,
    BookkeepersDetailsView,
    BookkeeperDeleteView,
)

app_name = "bookkeeper"

urlpatterns = [
    # path("api/", include("manager.urls.api"), name="manager-bookkeeper-api-urls"),
    path("", BookkeepersListView.as_view(), name="list"),
    path("<slug:slug>", BookkeepersDetailsView.as_view(), name="details"),
    path("<slug>/delete", BookkeeperDeleteView.as_view(), name="delete"),
]
