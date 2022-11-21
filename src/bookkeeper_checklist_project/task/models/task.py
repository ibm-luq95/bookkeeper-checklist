# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import TaskStatusEnum
from core.models import BaseModelMixin


class Task(BaseModelMixin):
    """Tasks for every job

    Args:
        BaseModelMixin (models.Model): The base django model mixin
    """

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

    objects = models.Manager()

    def __str__(self) -> str:
        return self.title
