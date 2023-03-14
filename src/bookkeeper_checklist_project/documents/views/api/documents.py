# -*- coding: utf-8 -*-#
import traceback

from rest_framework import parsers
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import ManagerApiPermission, BaseApiPermissionMixin
from core.utils import get_formatted_logger, debugging_print
from documents.models import Documents
from documents.serializers import DocumentSerializer

logger = get_formatted_logger()


class CreateDocumentApiView(APIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]

    perm_slug = "documents.document"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            debugging_print(data)
            serializer = DocumentSerializer(data=data)
            # raise APIException("Stop")
            # debugging_print(serializer.is_valid())
            if serializer.is_valid(raise_exception=True) is False:
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
                "user_error_msg": serializer.errors,
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


class DeleteDocumentApiView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "documents.document"

    def delete(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            document_id = data.get("documentId")
            # debugging_print(data)
            document_object = Documents.objects.get(pk=document_id)
            document_object.delete()
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
                "user_error_msg": ex,
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


class RetrieveDocumentApiView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "documents.document"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            document_id = data.get("documentId")
            document = Documents.objects.select_related().filter(pk=document_id).first()
            serializer = DocumentSerializer(instance=document)
            return Response(
                data={"document": serializer.data},
                status=status.HTTP_201_CREATED,
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
                "user_error_msg": "Error while retrieve document!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
