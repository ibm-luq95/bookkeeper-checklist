from django.urls import path
from assistant.views import BookkeepersListView, BookkeepersDetailsView

app_name = "bookkeeper"

urlpatterns = [
    path("", BookkeepersListView.as_view(), name="list"),
    path("<uuid:pk>", BookkeepersDetailsView.as_view(), name="details"),
]
