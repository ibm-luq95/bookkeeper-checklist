# -*- coding: utf-8 -*-#

from django.db import models
from django.utils.translation import gettext as _

# from client.models import Client
from core.choices import TaskStatusEnum, TaskTypeEnum
from core.constants.status_labels import CON_COMPLETED
from core.models import (
    BaseModelMixin,
    CreatedByMixin,
    StartAndDueDateMixin,
    StrModelMixin,
)
from jobs.models import Job


class Task(BaseModelMixin, StartAndDueDateMixin, StrModelMixin, CreatedByMixin):
    """Tasks for every job

    Args:
        BaseModelMixin (models.Model): The base django model mixin
    """

    # def __init__(self, *args, **kwargs):
    #     super(Task, self).__init__(*args, **kwargs)
    #     self.__original_model = self.model

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
    status = models.CharField(
        _("status"),
        max_length=15,
        null=True,
        blank=True,
        choices=TaskStatusEnum.choices,
        default=TaskStatusEnum.NOT_STARTED
        # db_column="status"
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
        help_text=_("Additional note for the task"),
    )

    def get_is_completed_label(self) -> str:
        if self.is_completed is True:
            return "Completed"
        else:
            return "Not completed"

    def save(self, *args, **kwargs):
        if self.status == CON_COMPLETED:
            self.is_completed = True
        else:
            self.is_completed = False
        super().save(*args, **kwargs)
