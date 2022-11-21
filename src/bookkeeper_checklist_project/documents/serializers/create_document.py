# -*- coding: utf-8 -*-#
from rest_framework import serializers
from documents.models import Documents


class CreateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        exclude = ("metadata", "is_deleted",)
        # depth = 1
