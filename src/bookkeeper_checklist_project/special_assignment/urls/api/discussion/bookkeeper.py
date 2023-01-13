# -*- coding: utf-8 -*-#
from django.urls import path
from special_assignment.views.api.discussion import CreateDiscussionBookkeeperApiView

app_name = "bookkeeper"

urlpatterns = [
    path(
        "create",
        CreateDiscussionBookkeeperApiView.as_view(),
        name="create",
    ),
]
