# -*- coding: utf-8 -*-#
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# from client.models import Client
from core.choices import TaskStatusEnum, TaskTypeEnum
from core.models import (
    BaseModelMixin,
    UserForeignKeyMixin,
    CreatedByMixin,
    StartAndDueDateMixin,
)
from jobs.models import Job


class Task(BaseModelMixin, StartAndDueDateMixin, CreatedByMixin):
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
    task_type = models.CharField(
        _("task type"),
        max_length=15,
        null=True,
        blank=True,
        choices=TaskTypeEnum.choices,
    )
    task_status = models.CharField(
        _("task status"),
        max_length=15,
        null=True,
        blank=True,
        choices=TaskStatusEnum.choices,
    )
    is_completed = models.BooleanField(_("is completed"), default=False)
    hints = models.CharField(
        _("hints"),
        max_length=60,
        null=True,
        blank=True,
        help_text=_("Hints help to this task"),
    )
    additional_notes = models.TextField(
        _("additional notes"),
        null=True,
        blank=True,
        help_text=_("Additional note " "for the task"),
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("bookkeeper:tasks:details", kwargs={"pk": self.pk})

    def get_is_completed_label(self) -> str:
        if self.is_completed is True:
            return "Completed"
        else:
            return "Not completed"
