# -*- coding: utf-8 -*-#
from rest_framework import serializers

from core.serializers import CreatedBySerializerMixin
from documents.models import Documents


class CreateDocumentSerializer(serializers.ModelSerializer, CreatedBySerializerMixin):
    # document_file = serializers.FileField(use_url=True, allow_empty_file=False)

    class Meta:
        model = Documents
        exclude = (
            "metadata",
            "is_deleted",
            "updated_at",
            "created_at",
            "deleted_at",
        )
        # depth = 1
