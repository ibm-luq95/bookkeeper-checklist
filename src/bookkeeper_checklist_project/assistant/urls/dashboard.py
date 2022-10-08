from django.urls import path, include
from assistant.views import DashboardView


urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    
]
