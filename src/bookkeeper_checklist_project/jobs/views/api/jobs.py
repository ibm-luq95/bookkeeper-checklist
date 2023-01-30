# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import get_formatted_logger
from jobs.models import Job

logger = get_formatted_logger(__name__)


class UpdateJobStatusApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            job_id = data.get("jobId")
            job_status = data.get("status")
            job = Job.objects.filter(pk=job_id)
            job.update(status=job_status)
            data = {"msg": "Status updated successfully!"}
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
