# -*- coding: utf-8 -*-#
from django.urls import path
from special_assignment.views.api.discussion import CreateDiscussionManagerApiView

app_name = "manager"

urlpatterns = [
    path(
        "create",
        CreateDiscussionManagerApiView.as_view(),
        name="create",
    ),
]
