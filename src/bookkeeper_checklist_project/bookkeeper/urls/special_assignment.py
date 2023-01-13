# -*- coding: utf-8 -*-#
from django.urls import path
from bookkeeper.views import SpecialAssignmentsListView, SpecialAssignmentDetailsView

app_name = "special_assignment"

urlpatterns = [
    path("", SpecialAssignmentsListView.as_view(), name="list"),
    path("<uuid:pk>", SpecialAssignmentDetailsView.as_view(), name="details"),
]
