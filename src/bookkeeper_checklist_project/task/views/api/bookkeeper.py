# -*- coding: utf-8 -*-#
import traceback

from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import get_formatted_logger, debugging_print
from task.models import Task
from task.serializers import TaskSerializer

logger = get_formatted_logger(__name__)


class TaskBookkeeperRetrieveAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            task_object = Task.objects.get(pk=data.get("taskId"))
            task_serializer = TaskSerializer(instance=task_object)
            return Response(
                data={"task": task_serializer.data},
                status=status.HTTP_201_CREATED,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": str(ex),
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while update task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class SetTaskCompletedBookkeeperApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            tasks = data.get("tasks")
            for task in tasks:
                task_object = Task.objects.get(pk=task)
                debugging_print(task_object.is_completed)
                task_object.is_completed = True
                task_object.save()
                job_object = task_object.job
                # check if all tasks done set the job completed
                if len(job_object.get_all_not_completed_tasks()) == 0:
                    job_object.status = "complete"
                    job_object.save()
            return Response(
                data={"msg": "Task set to completed successfully!", "tasks": tasks},
                status=status.HTTP_201_CREATED,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": str(ex),
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while update task!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
