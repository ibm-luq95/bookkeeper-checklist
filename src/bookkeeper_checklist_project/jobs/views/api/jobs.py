# -*- coding: utf-8 -*-#
import json
import traceback
from pprint import pprint

import stringcase
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from stringcase import sentencecase

from bookkeeper.models import BookkeeperProxy
from core.api.permissions import ManagerApiPermission, BaseApiPermissionMixin
from core.utils import get_formatted_logger, debugging_print
from jobs.models import Job, JobProxy
from jobs.serializers import CreateJobSerializer, JobSerializer
from task.models import Task

logger = get_formatted_logger()


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
            serializer = JobSerializer(data=json_data, context={"request": request})
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
            job_object = JobProxy.objects.get(pk=data.get("jobId"))
            serializer = JobSerializer(instance=job_object, context={"request": request})
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
            job_object = JobProxy.objects.get(pk=data.get("jobId"))
            del data["jobId"]
            # debugging_print(data)

            # serializer = JobSerializer(instance=job_object, data=data, partial=True)
            serializer = JobSerializer(
                instance=job_object, data=data, context={"request": request}, partial=True
            )
            serializer.is_valid(raise_exception=True)
            # if not serializer.is_valid(raise_exception=True):
            #     raise APIException(serializer.errors)
            # debugging_print(serializer.validated_data)
            # raise APIException("stop")
            # serializer.update(job_object, serializer.validated_data)
            serializer.save()
            # tasks = data.get("tasks")
            # bookkeepers = data.get("bookkeeper")

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
                # "user_error_msg": ex.detail,
                "user_error_msg": serializer.errors,
                # "user_error_msg": str(ex),
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while update job!",
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
            job_object = JobProxy.objects.get(pk=data.get("jobId"))
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
                    f"You cant delete '{job_object.title}', it contains un-completed "
                    f"{response_msg_data.get('not_completed_tasks')} "
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
            job = JobProxy.original_objects.filter(pk=job_id).first()
            # job.update(status=job_status)
            job.status = job_status
            job.save()
            data = {"msg": "Status updated successfully!", "status": job.status}
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


class UpdateEditableJobApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "jobs.job"

    def put(self, request: Request, *args, **kwargs):
        try:
            data = request.data
            job_object = JobProxy.objects.get(pk=data.get("pk"))
            is_managed_by = data.get("isManagedBy")
            # del data["jobId"]
            # debugging_print(data)
            # new_data = data.get("newData")
            # debugging_print(new_data)
            if is_managed_by is False:
                setattr(job_object, data.get("field"), data.get("newValue"))
            else:
                bookkeeper = BookkeeperProxy.objects.get(pk=data.get("newValue"))
                user = bookkeeper.user
                setattr(job_object, "managed_by", user)
            job_object.save()

            return Response(
                # data={"job": serializer.data, "msg": "Job updated successfully!"},
                data={
                    "job": job_object.pk,
                    "msg": f"{stringcase.sentencecase(data.get('field').capitalize())} updated successfully!",
                    "title": job_object.title,
                    "due_dte": job_object.due_date,
                },
                status=status.HTTP_200_OK,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(traceback.format_exc())
            # logger.error(ex.detail)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                # "user_error_msg": ex.detail,
                "user_error_msg": serializer.errors,
                # "user_error_msg": str(ex),
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while update job!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
