# -*- coding: utf-8 -*-#
import traceback

from rest_framework import parsers
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import ManagerApiPermission
from core.utils import get_formatted_logger
from documents.models import Documents
from documents.serializers import CreateDocumentSerializer

logger = get_formatted_logger(__name__)


class CreateDocumentManagerApiView(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        ManagerApiPermission,
    ]

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            serializer = CreateDocumentSerializer(data=data)
            # raise APIException("Stop")
            # debugging_print(serializer.is_valid())
            # debugging_print(data)
            if serializer.is_valid() is False:
                raise APIException(serializer.error_messages)
            # debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Document created successfully!"},
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
                "user_error_msg": "Error while create document!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class DeleteDocumentManagerApiView(APIView):
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticated,
        ManagerApiPermission,
    ]

    def delete(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            document_id = data.get("documentId")
            # debugging_print(data)
            document_object = Documents.objects.get(pk=document_id)
            document_object.soft_delete()
            return Response(
                data={"msg": "Document deleted successfully!"},
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
                "user_error_msg": "Error while delete document!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class RetrieveDocumentManagerView(APIView):
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticated,
        ManagerApiPermission,
    ]

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            document_id = data.get("documentId")
            document = Documents.objects.select_related().filter(pk=document_id).first()
            document_serializer = CreateDocumentSerializer(instance=document)
            return Response(
                data={"document": document_serializer.data},
                status=status.HTTP_201_CREATED,
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "user_error_msg": ex.detail,
                # "user_error_msg": serializer.error_messages,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while retrieve document!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
