# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import get_formatted_logger
from task.models import Task
from task.serializers import CreateTaskSerializer, TaskSerializer

logger = get_formatted_logger(__name__)


class CreateTaskManagerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

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


class RetrieveTaskManagerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

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
                "user_error_msg": serializer.error_messages,
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


class UpdateTaskManagerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            task_object = Task.objects.get(pk=data.get("taskId"))
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


class DeleteTaskManagerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

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
