# -*- coding: utf-8 -*-#
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView

from core.api.permissions import BaseApiPermissionMixin
from jobs.models import JobTemplate
from jobs.serializers import JobTemplateSerializer


class JobRetrieveTemplateApi(RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "jobs.jobtemplate"
    queryset = JobTemplate.objects.all()
    serializer_class = JobTemplateSerializer
