# -*- coding: utf-8 -*-#
from django.urls import path
from special_assignment.views.api.special_assignment import (
    UpdateSpecialAssignmentManagerApiView,
)

app_name = "manager"

urlpatterns = [
    path(
        "update",
        UpdateSpecialAssignmentManagerApiView.as_view(),
        name="update-status",
    ),
]
