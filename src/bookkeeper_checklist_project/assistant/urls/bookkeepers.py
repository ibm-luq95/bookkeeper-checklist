from django.urls import path
from assistant.views import BookkeepersListView


urlpatterns = [
    path("", BookkeepersListView.as_view(), name="bookkeeper-list-url"),
]
