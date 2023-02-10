# -*- coding: utf-8 -*-#
import django_filters
from documents.models import Documents


class DocumentsFilter(django_filters.FilterSet):
    class Meta:
        model = Documents
        fields = {
            "client": ["exact"],
            "job": ["exact"],
            "task": ["exact"],
            "document_section": ["exact"],
        }
