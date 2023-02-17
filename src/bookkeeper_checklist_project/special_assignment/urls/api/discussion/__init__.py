# -*- coding: utf-8 -*-#
from django.urls import path, include
from special_assignment.views.api.discussion import CreateDiscussionApiView

app_name = "discussion"

urlpatterns = [
    path(
        "create",
        CreateDiscussionApiView.as_view(),
        name="create",
    ),
]
