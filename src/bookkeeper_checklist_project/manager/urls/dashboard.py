from django.urls import path
from manager.views import DashboardHomeView

urlpatterns = [
    path("", DashboardHomeView.as_view(), name="dashboard"),
]
