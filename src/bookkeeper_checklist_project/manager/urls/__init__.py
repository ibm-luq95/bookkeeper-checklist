from django.urls import path, include

app_name = "manager"

urlpatterns = [
    path("dashboard/", include("manager.urls.dashboard"), name="dashboard-urls"),
    path("users/", include("manager.urls.users"), name="users-urls"),
    path("bookkeeper/", include("manager.urls.bookkeeper"), name="bookkeeper-urls"),
]
