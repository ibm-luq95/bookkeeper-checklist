from django.urls import path, include
from manager.views import BookkeepersListView, BookkeepersDetailsView

urlpatterns = [
    path("api/", include("manager.urls.api"), name="manager-bookkeeper-api-urls"),
    path("", BookkeepersListView.as_view(), name="bookkeeper-list"),
    path("<slug:slug>", BookkeepersDetailsView.as_view(), name="bookkeeper-details"),
]
