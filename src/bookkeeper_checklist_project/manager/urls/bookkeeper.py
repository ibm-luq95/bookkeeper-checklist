from django.urls import path
from manager.views import BookkeepersListView

urlpatterns = [
    path("", BookkeepersListView.as_view(), name="bookkeeper-list"),
]
