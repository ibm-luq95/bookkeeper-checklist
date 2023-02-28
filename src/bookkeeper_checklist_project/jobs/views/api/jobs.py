# -*- coding: utf-8 -*-#
import json
import traceback
from pprint import pprint

from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import ManagerApiPermission, BaseApiPermissionMixin
from core.utils import get_formatted_logger
from jobs.models import Job
from jobs.serializers import CreateJobSerializer, JobSerializer
from task.models import Task

logger = get_formatted_logger(__name__)


class CreateJobApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "jobs.job"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            json_data = json.dumps(data)
            json_data = json.loads(json_data)
            # pprint(data)
            serializer = JobSerializer(data=json_data)
            # debugging_print(serializer.is_valid())
            if not serializer.is_valid():
                raise APIException(serializer.errors)
            # pprint(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Job created successfully!"},
                status=status.HTTP_201_CREATED,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(serializer.errors)
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
                "user_error_msg": "Error while create job!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class RetrieveJobApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "jobs.job"

    def post(self, request: Request, *args, **kwargs):
        try:
            data = request.data
            job_object = Job.objects.get(pk=data.get("jobId"))
            serializer = JobSerializer(instance=job_object)
            return Response(
                data={"job": serializer.data},
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
                "user_error_msg": "Error while retrieve job!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class UpdateJobApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "jobs.job"

    def put(self, request: Request, *args, **kwargs):
        try:
            data = request.data
            job_object = Job.objects.get(pk=data.get("jobId"))
            del data["jobId"]
            serializer = JobSerializer(instance=job_object, data=data, partial=True)
            if not serializer.is_valid(raise_exception=True):
                raise APIException(serializer.errors)
            serializer.save()
            tasks = data.get("tasks")
            # bookkeepers = data.get("bookkeeper")

            # update bookkeeper
            # bookkeepers_objects_list = []
            # for bookkeeper in bookkeepers:
            #     bookkeepers_objects_list.append(bookkeeper)
            # job_object.bookkeeper.set(bookkeepers_objects_list)

            # update tasks
            tasks_objects_list = []
            for task in tasks:
                tasks_objects_list.append(Task.objects.get(pk=task))
            job_object.tasks.set(tasks_objects_list)
            return Response(
                data={"job": serializer.data, "msg": "Job updated successfully!"},
                status=status.HTTP_200_OK,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(traceback.format_exc())
            # logger.error(ex.detail)
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
                "user_error_msg": "Error while retrieve job!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class DeleteJobApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "jobs.job"

    def delete(self, request: Request, *args, **kwargs):
        try:
            response_msg_data = {
                "is_allowed_deleted": False,
                "msg": "",
                "not_completed_tasks": 0,
            }
            data = request.data
            job_object = Job.objects.get(pk=data.get("jobId"))
            # debugging_print(job_object.get_all_not_completed_tasks())
            response_msg_data["not_completed_tasks"] = len(
                job_object.get_all_not_completed_tasks()
            )
            # check if job contains tasks
            if job_object.tasks.count() <= 0:
                response_msg_data["is_allowed_deleted"] = True
                response_msg_data["msg"] = f"Job '{job_object}' deleted successfully"
                job_object.delete()
            else:
                response_msg_data["is_allowed_deleted"] = False
                response_msg_data["msg"] = (
                    f"You cant delete '{job_object.title}', it contains un-completed {response_msg_data.get('not_completed_tasks')} "
                    f"tasks!"
                )

            return Response(
                data=response_msg_data,
                status=status.HTTP_200_OK,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(traceback.format_exc())
            # logger.error(ex.detail)
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
                "user_error_msg": "Error while retrieve job!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class UpdateJobStatusApiView(APIView):
    permission_classes = (permissions.IsAuthenticated, BaseApiPermissionMixin)
    perm_slug = "jobs.job"

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            job_id = data.get("jobId")
            job_status = data.get("status")
            job = Job.objects.filter(pk=job_id)
            job.update(status=job_status)
            job = Job.original_objects.filter(pk=job_id)
            data = {"msg": "Status updated successfully!", "status": job.first().status}
            return Response(
                data=data,
                status=status.HTTP_200_OK,
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
                "user_error_msg": "Error while create job!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
