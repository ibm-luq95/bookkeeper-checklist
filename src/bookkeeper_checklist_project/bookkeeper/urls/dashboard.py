from django.urls import path, include
from bookkeeper.views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="bookkeeper-dashboard"),
    path("clients/", include("bookkeeper.urls.clients"), name="clients-urls"),
]
