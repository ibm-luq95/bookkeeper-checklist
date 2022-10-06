# -*- coding: utf-8 -*-#
from core.models import BaseModelMixin
from django.db import models
from core.choices import JobStatusEnum, JobTypeEnum
from django.utils.translation import gettext as _
from client.models import Client
from task.models import Task
from bookkeeper.models import Bookkeeper
from .help_messages import JOB_HELP_MESSAGES


class Job(BaseModelMixin):
    """This is the job for every bookkeeper and assistant

    Args:
        BaseModelMixin (models.Model): Django model base mixin
    """

    bookkeeper = models.ForeignKey(
        to=Bookkeeper,
        on_delete=models.PROTECT,
        related_name="jobs",
        # null=True,
        help_text=JOB_HELP_MESSAGES.get("bookkeeper"),
    )
    title = models.CharField(
        _("title"), max_length=70, null=False, help_text=JOB_HELP_MESSAGES.get("title")
    )
    note = models.TextField(
        _("note"), null=True, help_text=JOB_HELP_MESSAGES.get("note")
    )
    job_type = models.CharField(
        _("job_type"),
        choices=JobTypeEnum.choices,
        # default=JobTypeEnum.NO_TYPE,
        max_length=20,
        help_text=JOB_HELP_MESSAGES.get("job_type"),
    )
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=JobStatusEnum.choices,
        # default=JobStatusEnum.NOT_STARTED,
        help_text=JOB_HELP_MESSAGES.get("status"),
    )
    client = models.ForeignKey(
        to=Client,
        on_delete=models.PROTECT,
        null=True,
        help_text=JOB_HELP_MESSAGES.get("client"),
    )
    tasks = models.ManyToManyField(to=Task, help_text=JOB_HELP_MESSAGES.get("tasks"))
