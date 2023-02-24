# -*- coding: utf-8 -*-#
from django.urls import path, include
from special_assignment.views.api import (
    CreateSpecialAssignmentApiView,
    UpdateSpecialAssignmentApiView,
)

app_name = "special_assignment"

urlpatterns = [
    path("create", CreateSpecialAssignmentApiView.as_view(), name="create"),
    path(
        "update",
        UpdateSpecialAssignmentApiView.as_view(),
        name="update-status",
    ),
]
