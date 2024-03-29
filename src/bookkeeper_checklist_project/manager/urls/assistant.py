from django.urls import path
from manager.views import (
    AssistantListView,
    AssistantDetailsView,
    AssistantDeleteView,
    AssistantUpdateView,
    AssistantCreateView
)

app_name = "assistant"

urlpatterns = [
    path("", AssistantListView.as_view(), name="list"),
    path("create", AssistantCreateView.as_view(), name="create"),
    path("<uuid:pk>", AssistantDetailsView.as_view(), name="details"),
    path("delete/<uuid:pk>", AssistantDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", AssistantUpdateView.as_view(), name="update"),
]
