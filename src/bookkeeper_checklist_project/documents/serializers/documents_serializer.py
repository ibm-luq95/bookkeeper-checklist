# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.constants import EXCLUDED_FIELDS
from core.serializers import CreatedBySerializerMixin
from documents.models import Documents
from jobs.models import Job


class DocumentSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    # document_file = serializers.FileField(use_url=True, allow_empty_file=False)
    # job = serializers.PrimaryKeyRelatedField(
    #     queryset=Job.objects.all(), many=False, required=False
    # )

    class Meta:
        model = Documents
        exclude = EXCLUDED_FIELDS
        # depth = 1
