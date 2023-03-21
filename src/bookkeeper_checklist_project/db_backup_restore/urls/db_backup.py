# -*- coding: utf-8 -*-#
from django.urls import path

from db_backup_restore.views import (
    DBBackupListView,
    DBBackupCreateView,
    DBBackupDetailsView,
)

app_name = "backup"

urlpatterns = [
    path("", DBBackupListView.as_view(), name="list"),
    path("create", DBBackupCreateView.as_view(), name="create"),
    path("<uuid:pk>", DBBackupDetailsView.as_view(), name="details"),
]
