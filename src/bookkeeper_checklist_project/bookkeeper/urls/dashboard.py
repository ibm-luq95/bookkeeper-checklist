from django.urls import path, include
from bookkeeper.views import DashboardView

# app_name = "dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("clients/", include("bookkeeper.urls.clients"), name="clients-urls"),
    path("jobs/", include("bookkeeper.urls.jobs"), name="jobs-urls"),
    path("tasks/", include("bookkeeper.urls.tasks"), name="tasks-urls"),
    path(
        "special_assignment/",
        include("bookkeeper.urls.special_assignment"),
        name="special-assignment-urls",
    ),
]
