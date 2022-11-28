# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

# from client.models import Client
from core.choices import TaskStatusEnum
from core.models import BaseModelMixin, UserForeignKeyMixin
from jobs.models import Job


class Task(BaseModelMixin, UserForeignKeyMixin):
    """Tasks for every job

    Args:
        BaseModelMixin (models.Model): The base django model mixin
    """

    # client = models.ForeignKey(
    #     to=Client, on_delete=models.PROTECT, related_name="tasks", null=True, blank=True
    # )
    job = models.ForeignKey(
        to=Job, on_delete=models.PROTECT, related_name="tasks", null=True, blank=True
    )
    title = models.CharField(_("title"), max_length=80, null=True)
    status = models.CharField(
        _("status"),
        max_length=15,
        null=True,
        blank=True,
        choices=TaskStatusEnum.choices,
    )
    is_completed = models.BooleanField(_("is completed"), default=False)
    hints = models.CharField(_("hints"), max_length=60, null=True, blank=True)
    additional_notes = models.TextField(_("additional notes"), null=True, blank=True)
    start_date = models.DateField(_("start date"), null=True, blank=True)
    due_date = models.DateField(_("due date"))

    def __str__(self) -> str:
        return self.title
