from django.urls import path, include

app_name = "manager"

urlpatterns = [
    path("api/", include("manager.urls.api"), name="manager-bookkeeper-api-urls"),
    path("dashboard/", include("manager.urls.dashboard"), name="dashboard-urls"),
    path("users/", include("manager.urls.users"), name="users-urls"),
    path("bookkeeper/", include("manager.urls.bookkeeper"), name="bookkeeper-urls"),
    path("assistant/", include("manager.urls.assistant"), name="assistant-urls"),
    path("client/", include("manager.urls.client"), name="clients-urls"),
    path(
        "client_account/",
        include("manager.urls.client_account"),
        name="client-account-urls",
    ),
    path("jobs/", include("manager.urls.jobs"), name="jobs-urls"),
    path("task/", include("manager.urls.task"), name="task-urls"),
    path(
        "company_services/",
        include("manager.urls.company_services"),
        name="company-services-urls",
    ),
    path(
        "important_contact/",
        include("manager.urls.important_contact"),
        name="important-contact-urls",
    ),
    path(
        "special_assignment/",
        include("manager.urls.special_assignment"),
        name="special-assignment-urls",
    ),
]
