# -*- coding: utf-8 -*-#
import traceback
from pprint import pprint

from django.urls import reverse_lazy
from rest_framework import permissions, generics
from rest_framework import status
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import BookkeeperApiPermission, CheckOwnerPermission
from core.utils import get_formatted_logger
from task.models import Task
from task.serializers import TaskSerializer, CreateTaskSerializer

logger = get_formatted_logger(__name__)


class TaskBookkeeperRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    ]
    serializer_class = TaskSerializer
    queryset = Task.objects.select_related().all()

    def get_object(self):
        qs = self.get_queryset()
        obj = get_object_or_404(queryset=qs, pk=self.request.GET.get("task"))
        return obj

    # def post(self, request: Request, *args, **kwargs):
    #     serializer = ""
    #     try:
    #         data = request.data
    #         print("@@@@@@@@@@@@@@@@@@@@@")
    #         task_object = Task.objects.get(pk=data.get("taskId"))
    #         task_serializer = TaskSerializer(instance=task_object)
    #         # debugging_print(task_serializer.data)
    #         return Response(
    #             data={"task": task_serializer.data},
    #             status=status.HTTP_201_CREATED,
    #         )
    #     except APIException as ex:
    #         # logger.error("API Exception")
    #         logger.error(ex)
    #         response_data = {
    #             "status": status.HTTP_400_BAD_REQUEST,
    #             # "user_error_msg": ex.detail,
    #             "user_error_msg": str(ex),
    #         }
    #         return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as ex:
    #         # debugging_print(ex)
    #         logger.error(traceback.format_exc())
    #         response_data = {
    #             "status": status.HTTP_400_BAD_REQUEST,
    #             "error": str(ex),
    #             "user_error_msg": "Error while update task!",
    #         }
    #         return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class SetTaskCompletedBookkeeperApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    )

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            tasks = data.get("tasks")
            current_user = request.user

            for task in tasks:
                task_object = Task.objects.get(pk=task)
                if current_user != task_object.user:
                    raise PermissionDenied(
                        {"user_error_msg": "You dont have permission to update this task!"}
                    )
                task_object.is_completed = True
                task_object.task_status = "completed"
                task_object.save()
                job_object = task_object.job
                # check if all tasks done set the job completed
                if len(job_object.get_all_not_completed_tasks()) == 0:
                    job_object.status = "complete"
                    job_object.save()
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


class CreateTaskBookkeeperApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    )

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            serializer = CreateTaskSerializer(data=data)
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


class UpdateTaskBookkeeperApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    )

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            current_user = request.user
            task_object = Task.objects.get(pk=data.get("id"))
            if current_user != task_object.user:
                raise PermissionDenied(
                    {"user_error_msg": "You dont have permission to update this task!"}
                )
            serializer = CreateTaskSerializer(data=data, instance=task_object)
            if not serializer.is_valid():
                raise APIException(serializer.errors)
            # debugging_print(serializer.validated_data)
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
                "user_error_msg": "Error while create task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class DeleteTaskBookkeeperApiView(APIView, CheckOwnerPermission):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
        CheckOwnerPermission,
    )

    def delete(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            pprint(reverse_lazy("manager:bookkeeper:details"))
            data = request.data
            current_user = request.user
            task_object = Task.objects.get(pk=data.get("taskId"))
            if current_user != task_object.user:
                raise PermissionDenied(
                    {"user_error_msg": "You dont have permission to delete this task!"}
                )

            # task_object.delete()
            return Response(
                data={"msg": "Task deleted successfully!"}, status=status.HTTP_200_OK
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
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
                "user_error_msg": "Error while create task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
