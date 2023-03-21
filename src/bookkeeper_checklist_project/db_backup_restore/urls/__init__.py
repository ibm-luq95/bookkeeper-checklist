# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "db_backup_restore"

urlpatterns = [
    path("backup/", include("db_backup_restore.urls.db_backup"), name="db-backup-urls"),
    path("restore/", include("db_backup_restore.urls.db_restore"), name="db-restore-urls"),
]
