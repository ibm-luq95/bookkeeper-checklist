# -*- coding: utf-8 -*-#
from django.urls import path
from special_assignment.views.api.special_assignment import (
    UpdateSpecialAssignmentBookkeeperApiView,
)

app_name = "bookkeeper"

urlpatterns = [
    path(
        "update",
        UpdateSpecialAssignmentBookkeeperApiView.as_view(),
        name="update-status",
    ),
]
