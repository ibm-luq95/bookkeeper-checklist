# -*- coding: utf-8 -*-#
from django.urls import path
from assistant.views import ImportantContactListView, ImportantContactCreateView

app_name = "important_contact"

urlpatterns = [
    path("", ImportantContactListView.as_view(), name="list"),
    path("create", ImportantContactCreateView.as_view(), name="create"),
]
