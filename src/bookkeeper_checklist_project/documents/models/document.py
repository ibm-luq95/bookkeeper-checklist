# -*- coding: utf-8 -*-#
import secrets

from django.db import models
from django.utils.translation import gettext as _

from client.models import ClientProxy
from core.choices import DocumentTypesEnum
from core.models import BaseModelMixin, CreatedByMixin, GeneralStatusFieldMixin
from jobs.models import JobProxy
from task.models import Task


# def saved_document_file_path(instance, filename):
#     file_path = ""
#     file_suffix = secrets.token_urlsafe(7)
#     if instance.document_section == "client":
#         # if instance.client:
#         file_path = f"documents/clients/{instance.client.pk}/{file_suffix}_{filename}"
#     elif instance.document_section == "task":
#         # if instance.task:
#         file_path = f"documents/tasks/{instance.task.pk}/{file_suffix}_{filename}"
#     elif instance.document_section == "job":
#         # if instance.job:
#         file_path = f"documents/jobs/{instance.job.pk}/{file_suffix}_{filename}"
#
#     return file_path
def saved_document_file_path(instance, filename):
    file_suffix = secrets.token_urlsafe(7)
    return f"documents/{file_suffix}_{filename}"


class Documents(BaseModelMixin, GeneralStatusFieldMixin, CreatedByMixin):
    title = models.CharField(_("title"), max_length=70, null=False, blank=False)
    document_section = models.CharField(
        _("document section"),
        max_length=15,
        null=True,
        blank=True,
        choices=DocumentTypesEnum.choices,
    )
    document_file = models.FileField(
        _("document file"), upload_to=saved_document_file_path
    )

    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documents",
    )
    job = models.ForeignKey(
        to=JobProxy, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents"
    )
    task = models.ForeignKey(
        to=Task, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents"
    )

    # def delete(self, *args, **kwargs):
    #     self.document_file.storage.delete(self.document_file.name)
    #     super(Documents, self).delete(*args, **kwargs)
