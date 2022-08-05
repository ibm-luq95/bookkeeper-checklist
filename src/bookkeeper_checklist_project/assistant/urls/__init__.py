from django.urls import path, include

app_name = "assistant"

urlpatterns = [
    path("dashboard/", include("assistant.urls.dashboard"), name="dashboard-urls"),
    path("bookkeepers/", include("assistant.urls.bookkeepers"), name="bookkeepers-urls"),
]
