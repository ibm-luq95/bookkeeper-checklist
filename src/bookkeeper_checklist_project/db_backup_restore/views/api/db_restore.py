# -*- coding: utf-8 -*-#
import traceback
from pathlib import Path

import pyminizip
from django.conf import settings
from django.core import management
from django.core.management.commands import loaddata
from django.db import transaction
from django.utils import timezone
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger
from db_backup_restore.models import DBBackup

logger = get_formatted_logger()


class RestoreDBApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "db_backup_restore.dbbackup"

    def post(self, request: Request, *args, **kwargs):
        try:
            data = request.data
            EXCLUDED = (
                "auth.Permission",
                "contenttypes.ContentType",
                "sessions.Session",
            )
            pk = data.get("pk")
            with transaction.atomic():
                backup_object = DBBackup.objects.get(pk=pk)
                dist_folder = settings.BASE_DIR / "db_backups"
                file_name = dist_folder / backup_object.backup_path.name
                if not file_name.exists():
                    raise APIException("Backup file not exists!")
                password = settings.BACKUP_KEY
                pyminizip.uncompress(
                    file_name.as_posix(), password, dist_folder.as_posix(), 0
                )
                json_file_name = file_name.as_posix().replace(".zip", ".yaml")
                management.call_command(
                    loaddata.Command(),
                    json_file_name,
                    # "--ignorenonexistent",
                    exclude=EXCLUDED,
                    format="yaml",
                )
                Path(json_file_name).unlink()
                backup_object.is_restored = True
                backup_object.restored_at = timezone.now()
                backup_object.save()
                return Response(
                    data={"msg": "DB restored successfully!"},
                    status=status.HTTP_201_CREATED,
                )
        except APIException as ex:
            # logger.error("API Exception")
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "user_error_msg": ex.detail,
                # "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while restore db!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
