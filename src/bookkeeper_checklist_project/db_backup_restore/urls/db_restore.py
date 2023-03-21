# -*- coding: utf-8 -*-#
from django.urls import path

from db_backup_restore.views import RestoreDBDetailsView
from db_backup_restore.views.api import RestoreDBApiView

app_name = "restore"

urlpatterns = [
    path("<uuid:pk>", RestoreDBDetailsView.as_view(), name="prepare-restore"),
    path("api-restore", RestoreDBApiView.as_view(), name="api-restore"),
]
