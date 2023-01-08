# -*- coding: utf-8 -*-#
import json
import traceback

from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework import authentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import parsers

from core.utils import get_formatted_logger, debugging_print
from special_assignment.models import Discussion
from special_assignment.serializers import DiscussionSerializer

logger = get_formatted_logger(__name__)


class CreateDiscussionManagerApiView(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    # parser_classes = [parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            debugging_print(data.keys())
            serializer = DiscussionSerializer(data=data)
            # raise APIException("Stop")
            # debugging_print(serializer.is_valid())
            # debugging_print(data)
            if serializer.is_valid() is False:
                raise APIException(serializer.error_messages)
            debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Reply created successfully!"},
                status=status.HTTP_201_CREATED,
            )

        except Exception as ex:
            debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": serializer.errors,
                "user_error_msg": "Error while create discussion!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
