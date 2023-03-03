from core.admin import BaseAdminModelMixin
from django.contrib import admin
from documents.models import Documents, DocumentTemplate


@admin.register(Documents)
class DocumentAdmin(BaseAdminModelMixin):
    pass


@admin.register(DocumentTemplate)
class DocumentTemplateAdmin(BaseAdminModelMixin):
    pass
