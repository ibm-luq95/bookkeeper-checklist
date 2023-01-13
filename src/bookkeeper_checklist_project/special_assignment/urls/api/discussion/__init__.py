# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "discussion"

urlpatterns = [
    path(
        "manager/",
        include("special_assignment.urls.api.discussion.manager"),
        name="manager-discussion-api-urls",
    ),
    path(
        "bookkeeper/",
        include("special_assignment.urls.api.discussion.bookkeeper"),
        name="bookkeeper-discussion-api-urls",
    ),

]
