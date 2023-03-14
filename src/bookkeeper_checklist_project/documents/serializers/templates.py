# -*- coding: utf-8 -*-#
from rest_framework import serializers
from core.serializers.job_template_create import SaveRelatedJobTemplateSerializer

# from core.constants import EXCLUDED_FIELDS
from documents.models import DocumentTemplate


class DocumentTemplateSerializer(
    SaveRelatedJobTemplateSerializer, serializers.ModelSerializer
):
    class Meta:
        model = DocumentTemplate
        fields = ["title", "template_file", "job_template"]
