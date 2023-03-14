# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions, generics, parsers
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import ManagerApiPermission, BaseApiPermissionMixin
from core.constants.status_labels import CON_COMPLETED
from core.utils import get_formatted_logger, debugging_print
from task.models import TaskTemplate, TaskItem
from task.serializers import TaskItemSerializer, TaskSerializer, TaskTemplateSerializer
from pprint import pprint

logger = get_formatted_logger(__name__)


class TaskTemplateRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "task.tasktemplate"
    serializer_class = TaskTemplateSerializer
    queryset = TaskTemplate.objects.all()


class TaskTemplateDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "task.tasktemplate"
    serializer_class = TaskTemplateSerializer
    queryset = TaskTemplate.objects.all()


class CreateTaskTemplateApiView(generics.CreateAPIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "task.tasktemplate"
    serializer_class = TaskTemplateSerializer


class CreateTaskItemApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "task.taskitem"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            task = data.get("task")
            task_template_obj = TaskTemplate.objects.get(pk=task)
            del data["task"]
            serializer = TaskItemSerializer(data=data)
            if not serializer.is_valid(raise_exception=True):
                raise APIException(serializer.errors)
            serializer.save()
            task_template_obj.items.add(serializer.instance)
            task_template_obj.save()
            return Response(
                data={
                    "msg": "Task item created successfully!",
                    "taskItem": serializer.validated_data,
                    "taskParentPK": task_template_obj.pk,
                },
                status=status.HTTP_200_OK,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "user_error_msg": ex.detail,
                # "user_error_msg": str(ex),
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while create new task item!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
