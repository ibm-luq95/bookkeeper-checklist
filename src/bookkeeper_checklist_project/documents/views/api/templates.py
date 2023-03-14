# -*- coding: utf-8 -*-#
import traceback

from rest_framework import permissions, generics, parsers
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.permissions import ManagerApiPermission, BaseApiPermissionMixin
from core.constants.status_labels import CON_COMPLETED
from core.utils import get_formatted_logger, debugging_print
from documents.serializers import DocumentTemplateSerializer
from pprint import pprint


class CreateDocumentTemplateApiView(generics.CreateAPIView):
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    ]
    perm_slug = "documents.documenttemplate"
    serializer_class = DocumentTemplateSerializer
