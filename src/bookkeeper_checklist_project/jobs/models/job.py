# -*- coding: utf-8 -*-#
import textwrap

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _

from client.models import Client
from core.choices import JobStatusEnum, JobTypeEnum
from core.models import BaseModelMixin, CreatedByMixin, StartAndDueDateMixin

# from task.models import Task
from .help_messages import JOB_HELP_MESSAGES


class Job(BaseModelMixin, StartAndDueDateMixin, CreatedByMixin):
    """This is the job for every bookkeeper and assistant

    Args:
        BaseModelMixin (models.Model): Django model base mixin
    """

    client = models.ForeignKey(
        to=Client,
        on_delete=models.PROTECT,  # TODO: check if this should be null not protected
        null=True,
        blank=True,
        related_name="jobs",
        help_text=JOB_HELP_MESSAGES.get("client"),
    )
    managed_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="jobs",
        null=True,
        blank=True,
        help_text=JOB_HELP_MESSAGES.get("managed_by"),
    )
    title = models.CharField(
        _("title"), max_length=100, null=False, help_text=JOB_HELP_MESSAGES.get("title")
    )
    slug = models.SlugField(_("slug"), max_length=250, null=True, blank=True)
    description = models.TextField(
        _("description"),
        null=True,
        blank=True,
        help_text=JOB_HELP_MESSAGES.get("description"),
    )
    job_type = models.CharField(
        _("job type"),
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

    # tasks = models.ManyToManyField(to=Task, help_text=JOB_HELP_MESSAGES.get("tasks"))
    note = models.TextField(
        _("note"), null=True, help_text=JOB_HELP_MESSAGES.get("note"), blank=True
    )

    # not_filtered_objects = JobManager()
    # objects = JobManager()

    class Meta(BaseModelMixin.Meta):
        permissions = BaseModelMixin.Meta.permissions + [
            ("list_abstract_job_template", "List abstract job template")
        ]

    def __str__(self) -> str:
        # return self.title
        return textwrap.shorten(self.title, width=40, placeholder="...")

    # def get_absolute_url(self):
    #     return reverse("manager:jobs:details", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # self.bookkeeper.clients.add(self.client)
        # self.bookkeeper.save()
        super(Job, self).save(*args, **kwargs)

    def get_all_not_completed_tasks(self):
        filtered = filter(lambda task: task.is_completed is False, self.tasks.all())
        return tuple(filtered)

    def is_job_pass_due(self) -> bool:
        now = timezone.now().date()
        if self.due_date > now:
            return True
        else:
            return False

    # def get_all_assigned_users(self) -> list:
    #     all_users = []
    #     if self.bookkeeper.all():
    #         for bookkeeper in self.bookkeeper.all():
    #             all_users.append(bookkeeper)
    #
    #     if self.assistants.all():
    #         for assistant in self.assistants.all():
    #             all_users.append(assistant)
    #     return all_users
