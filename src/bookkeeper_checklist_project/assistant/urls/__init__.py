from django.urls import path, include

app_name = "assistant"

urlpatterns = [
    path("dashboard/", include("assistant.urls.dashboard"), name="dashboard-urls"),
    path("bookkeepers/", include("assistant.urls.bookkeepers"), name="bookkeepers-urls"),
    path("client/", include("assistant.urls.client"), name="client-urls"),
    path("job/", include("assistant.urls.job"), name="job-urls"),
    path(
        "important_contact/",
        include("assistant.urls.important_contact"),
        name="important_contact-urls",
    ),
]
