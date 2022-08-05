from django.urls import path, include

app_name = "bookkeeper"

urlpatterns = [
    path("dashboard/", include("bookkeeper.urls.dashboard"), name="dashboard-urls"),
]