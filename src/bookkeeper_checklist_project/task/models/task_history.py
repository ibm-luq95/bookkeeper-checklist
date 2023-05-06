from django.db import models
from django.utils.translation import gettext as _

from core.choices import TaskStatusEnum
from core.models import BaseModelMixin
from task.models import TaskProxy


class TaskHistory(BaseModelMixin):
    task = models.ForeignKey(
        to=TaskProxy,
        on_delete=models.CASCADE,
        related_name="history",
        null=True,
        blank=True,
    )
    previous_status = models.CharField(
        _("previous status"),
        max_length=15,
        choices=TaskStatusEnum.choices,
    )
    is_archived = models.BooleanField(_("is archived"), default=False)

    def __str__(self):
        return f"Task history for: {self.task.title}"
