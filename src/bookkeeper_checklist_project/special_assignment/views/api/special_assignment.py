# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions, parsers
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from special_assignment.models import SpecialAssignment
from special_assignment.serializers import SpecialAssignmentSerializer
from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger, debugging_print

logger = get_formatted_logger(__name__)


class CreateSpecialAssignmentApiView(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [
        # permissions.IsAdminUser,
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "special_assignment.specialassignment"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            serializer = SpecialAssignmentSerializer(data=data)
            # debugging_print(serializer.is_valid())
            # debugging_print(data)
            if not serializer.is_valid(raise_exception=True):
                raise APIException(serializer.error_messages)
            # debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Special assignment created successfully!"},
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
                "user_error_msg": "Error while create company services!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class UpdateSpecialAssignmentApiView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "special_assignment.specialassignment"

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            special_assignment_pk = data.get("special_assignment")
            status_lbl = data.get("status")
            special_assignment_object = SpecialAssignment.objects.get(
                pk=special_assignment_pk
            )
            special_assignment_object.status = status_lbl
            special_assignment_object.save()

            return Response(
                data={"msg": "Update SpecialAssignment successfully!"},
                status=status.HTTP_200_OK,
            )

        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": serializer.errors,
                "user_error_msg": "Error while create discussion!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
