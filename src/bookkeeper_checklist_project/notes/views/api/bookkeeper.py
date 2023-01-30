# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import get_formatted_logger
from core.api.permissions import BookkeeperApiPermission
from notes.models import Note
from notes.serializers import CreateNoteSerializer, NoteSerializer

logger = get_formatted_logger(__name__)


class CreateNoteBookkeeperApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    )

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            # debugging_print(data)
            serializer = CreateNoteSerializer(data=data)
            # debugging_print(serializer.is_valid())
            # debugging_print(data)
            if not serializer.is_valid():
                raise APIException(serializer.error_messages)
            # debugging_print(serializer.validated_data)
            serializer.save()
            return Response(
                data={"msg": "Note created successfully!"}, status=status.HTTP_201_CREATED
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
                "user_error_msg": "Error while create note!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class RetrieveNoteBookkeeperApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    )

    def post(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            note_id = data.get("noteId")
            note_object = Note.objects.get(pk=note_id)
            serializer = NoteSerializer(instance=note_object)
            return Response(data={"note": serializer.data}, status=status.HTTP_200_OK)
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
                "user_error_msg": "Error while retriever note!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class UpdateNoteBookkeeperApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    )

    def put(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            note_id = data.get("id")
            user = request.user
            note_object = Note.objects.get(pk=note_id)
            if note_object.created_by != user:
                raise PermissionDenied(
                    {"user_error_msg": "You dont have permission to update!"}
                )
            serializer = NoteSerializer(instance=note_object, data=data)
            if not serializer.is_valid():
                raise APIException(detail=serializer.errors)
            serializer.save()
            return Response(
                data={"msg": "Note updated successfully"}, status=status.HTTP_200_OK
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
                "user_error_msg": "Error while update note!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class DeleteNoteBookkeeperApiView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BookkeeperApiPermission,
    )

    def delete(self, request: Request, *args, **kwargs):
        serializer = ""
        try:
            data = request.data
            user = request.user
            note_id = data.get("noteId")
            note_object = Note.objects.get(pk=note_id)
            if note_object.created_by != user:
                raise PermissionDenied(
                    {"user_error_msg": "You dont have permission to delete!"}
                )
            # note_object.soft_delete()
            note_object.delete()

            return Response(
                data={"msg": "Note deleted successfully!"}, status=status.HTTP_200_OK
            )
        except APIException as ex:
            # logger.error("API Exception")
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "user_error_msg": ex.detail,
                # "user_error_msg": serializer.error_emessages,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while delete note!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
