from client.models import Client
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _

from . import TaskItem


class TaskTypeEnum(models.TextChoices):
    NO_TYPE = "no_type", _("No Type")
    RECURRING = "recurring", _("Recurring")
    WEEKLY = "weekly", _("Weekly")
    MONTHLY = "monthly", _("Monthly")
    QUARTERLY = "quarterly", _("Quarterly")
    YEARLY = "yearly", _("Yearly")
    ONE_TIME = "one_time", _("One Time")
    URGENT = "urgent", _("Urgent")


class TaskStatusEnum(models.TextChoices):
    NOT_STARTED = "not_started", _("Not Started")
    IN_PROGRESS = "in_progress", _("In progress")
    PAST_DUE = "past_due", _("Past Due")
    COMPLETE = "complete", _("Complete")


class Task(BaseModelMixin):
    title = models.CharField(_("title"), max_length=70, null=False)
    note = models.TextField(_("note"), null=True)
    task_type = models.CharField(
        _("task_type"), choices=TaskTypeEnum.choices, default=TaskTypeEnum.NO_TYPE, max_length=20
    )
    task_status = models.CharField(
        _("task_status"),
        max_length=20,
        choices=TaskStatusEnum.choices,
        default=TaskStatusEnum.NOT_STARTED,
    )
    due_date = models.DateField(_("due_date"), null=False)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True)
    task_items = models.ManyToManyField(to=TaskItem)
