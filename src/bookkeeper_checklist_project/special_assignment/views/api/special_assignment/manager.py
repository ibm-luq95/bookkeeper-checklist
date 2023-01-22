# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import ManagerApiPermission
from core.utils import get_formatted_logger
from special_assignment.models import SpecialAssignment

logger = get_formatted_logger(__name__)


class UpdateSpecialAssignmentManagerApiView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        ManagerApiPermission,
    ]

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
