# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from company_services.serializers import CreateCompanyServicesSerializer
from core.api.permissions import ManagerApiPermission
from core.utils import get_formatted_logger

logger = get_formatted_logger(__name__)


class CreateCompanyServiceManagerApiView(APIView):
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticated,
        ManagerApiPermission,
    ]

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            serializer = CreateCompanyServicesSerializer(data=data)
            # debugging_print(serializer.is_valid())
            # debugging_print(data)
            if not serializer.is_valid():
                raise APIException(serializer.error_messages)
            # debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Services created successfully!"},
                status=status.HTTP_201_CREATED,
            )
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
                "user_error_msg": "Error while create company services!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
