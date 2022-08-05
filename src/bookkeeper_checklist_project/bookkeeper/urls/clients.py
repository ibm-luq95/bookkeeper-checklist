from django.urls import path, include
from bookkeeper.views import ClientsListView, ClientsDetailsView


urlpatterns = [
    path("", ClientsListView.as_view(), name="clients-list"),
    path("<int:pk>", ClientsDetailsView.as_view(), name="clients-details"),
]
