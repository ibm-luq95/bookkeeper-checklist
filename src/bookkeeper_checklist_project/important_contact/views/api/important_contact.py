# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from important_contact.models import ImportantContact
from important_contact.serializers import ImportantContactSerializer
from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger, debugging_print

logger = get_formatted_logger(__name__)


class CreateImportantContactApiView(APIView):
    permission_classes = [
        # permissions.IsAdminUser,
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "important_contact.importantcontact"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            serializer = ImportantContactSerializer(data=data)
            # debugging_print(serializer.is_valid())
            # debugging_print(data)
            if not serializer.is_valid(raise_exception=True):
                raise APIException(serializer.error_messages)
            # debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Contact created successfully!"},
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
                "user_error_msg": "Error while create company services!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class UpdateImportantContactApiView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        BaseApiPermissionMixin,
    ]
    perm_slug = "important_contact.importantcontact"

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data.get("client"))
            important_contact_client = (
                ImportantContact.objects.select_related()
                .filter(client__pk=data.get("client"))
                .first()
            )
            serializer = ImportantContactSerializer(
                data=data, instance=important_contact_client
            )
            if not serializer.is_valid():
                raise APIException(serializer.errors)
            serializer.save()
            return Response(
                data={"msg": "Important Contact updated successfully!"},
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
                "user_error_msg": "Error while update important contact!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class RetrieveImportantContactApiView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        BaseApiPermissionMixin,
    ]
    perm_slug = "important_contact.importantcontact"

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            important_contact_pk = data.get("importantContactId")
            important_contact_obj = (
                ImportantContact.objects.select_related()
                .filter(pk=important_contact_pk)
                .first()
            )
            serializer = ImportantContactSerializer(instance=important_contact_obj)

            return Response(
                data={"important_contact": serializer.data},
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
                "user_error_msg": "Error while retrieve important contact!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
