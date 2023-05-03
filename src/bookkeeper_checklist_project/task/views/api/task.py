# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions, generics
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import ManagerApiPermission, BaseApiPermissionMixin
from core.constants.status_labels import CON_COMPLETED
from core.utils import get_formatted_logger, debugging_print
from task.models import Task
from task.serializers import CreateTaskSerializer, TaskSerializer
from pprint import pprint

logger = get_formatted_logger()


class CreateTaskApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "task.task"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            pprint(data)
            serializer = TaskSerializer(data=data)
            if not serializer.is_valid():
                raise APIException(serializer.error_messages)
            # debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Task created successfully!"}, status=status.HTTP_201_CREATED
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while create task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class RetrieveTaskApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "task.task"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            task_object = Task.objects.get(pk=data.get("taskId"))
            serializer = TaskSerializer(instance=task_object)
            return Response(data={"task": serializer.data}, status=status.HTTP_200_OK)
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while retrieve task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class UpdateTaskApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "task.task"

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            task_object = Task.objects.get(pk=data.get("id"))
            serializer = TaskSerializer(instance=task_object, data=data)
            if not serializer.is_valid(raise_exception=True):
                raise APIException(serializer.errors)
            # debugging_print(task_object.job)
            # debugging_print(task_object.job)
            serializer.save()
            return Response(
                data={"msg": "Task updated successfully!"}, status=status.HTTP_200_OK
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while update task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class DeleteTaskApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "task.task"

    def delete(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            task_object = Task.objects.get(pk=data.get("taskId"))
            task_object.delete()
            return Response(
                data={"msg": "Task deleted successfully!"}, status=status.HTTP_200_OK
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "user_error_msg": ex.detail,
                # "user_error_msg": serializer.ex,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while update task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class SetTaskCompletedApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "task.task"

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            tasks = data.get("tasks")
            current_user = request.user

            for task in tasks:
                task_object = Task.objects.get(pk=task)
                # if current_user != task_object.created_by:
                #     raise PermissionDenied(
                #         {"user_error_msg": "You don't have permission to update this task!"}
                #     )
                task_object.is_completed = True
                task_object.status = CON_COMPLETED
                task_object.save()
                job_object = task_object.job
                # check if all tasks done set the job completed
                # if len(job_object.get_all_not_completed_tasks()) == 0:
                #     job_object.status = CON_COMPLETED
                #     job_object.save()
            return Response(
                data={"msg": "Task set to completed successfully!", "tasks": tasks},
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
                "user_error_msg": "Error while update task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "task.task"
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_object(self):
        qs = self.get_queryset()
        obj = get_object_or_404(queryset=qs, pk=self.request.GET.get("task"))
        return obj
