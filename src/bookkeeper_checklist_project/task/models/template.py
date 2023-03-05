# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.choices import TaskTypeEnum, TaskStatusEnum
from core.models import BaseModelMixin, StartAndDueDateMixin, StrModelMixin
from task.models import TaskItem


class TaskTemplate(BaseModelMixin, StartAndDueDateMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=100)
    notes = models.CharField(_("notes"), max_length=200, null=True, blank=True)
    task_type = models.CharField(
        _("task type"),
        max_length=15,
        null=True,
        blank=True,
        choices=TaskTypeEnum.choices,
    )
    status = models.CharField(
        _("task status"),
        max_length=15,
        null=True,
        blank=True,
        choices=TaskStatusEnum.choices,
    )
    attachment = models.FileField(
        _("attachment"), upload_to="task_templates/", null=True, blank=True
    )
    items = models.ManyToManyField(to=TaskItem, related_name="task_template", blank=True)
