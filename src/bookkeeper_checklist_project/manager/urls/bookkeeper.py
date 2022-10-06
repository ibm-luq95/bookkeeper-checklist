from django.urls import path
from manager.views import BookkeepersListView, BookkeepersDetailsView

urlpatterns = [
    path("", BookkeepersListView.as_view(), name="bookkeeper-list"),
    path("<slug:slug>", BookkeepersDetailsView.as_view(), name="bookkeeper-details"),
]
