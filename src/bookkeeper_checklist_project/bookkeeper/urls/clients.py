from django.urls import path, include
from bookkeeper.views import ClientsListView, ClientsDetailsView

app_name = "client"

urlpatterns = [
    path("", ClientsListView.as_view(), name="list"),
    path("<uuid:pk>", ClientsDetailsView.as_view(), name="details"),
]
