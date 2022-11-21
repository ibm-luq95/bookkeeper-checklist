# -*- coding: utf-8 -*-#
import secrets

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from client.models import Client
from core.choices import DocumentTypesEnum
from core.models import BaseModelMixin
from jobs.models import Job
from task.models import Task


def saved_document_file_path(instance, filename):

    file_path = ""
    file_suffix = secrets.token_urlsafe(7)
    if instance.client:
        file_path = f"documents/clients/{instance.client.name}/{file_suffix}_{filename}"
    if instance.task:
        file_path = f"documents/tasks/{instance.task.pk}/{file_suffix}_{filename}"
    if instance.job:
        file_path = f"documents/jobs/{instance.job.title}/{file_suffix}_{filename}"

    return file_path


class Documents(BaseModelMixin):
    title = models.CharField(_("title"), max_length=70, null=False, blank=False)
    document_section = models.CharField(
        _("document section"),
        max_length=15,
        null=True,
        blank=True,
        choices=DocumentTypesEnum.choices,
    )
    document_file = models.FileField(_("document file"), upload_to=saved_document_file_path)

    client = models.ForeignKey(
        to=Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documents",
    )
    job = models.ForeignKey(
        to=Job, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents"
    )
    task = models.ForeignKey(
        to=Task, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents"
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.SET_NULL, related_name="documents", null=True
    )

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("documents:manager:details", kwargs={"pk": self.pk})
