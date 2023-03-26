# -*- coding: utf-8 -*-#

from django.db import models
from django.utils.translation import gettext as _

from core.choices import JobStatusEnum, JobTypeEnum, JobStateEnum
from core.models import BaseModelMixin, DueDateOnlyMixin, StrModelMixin
from documents.models import DocumentTemplate
from jobs.models import JobCategory
from notes.models import NoteTemplate
from task.models import TaskTemplate


class JobTemplate(BaseModelMixin, DueDateOnlyMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=150)
    description = models.TextField(_("description"))
    job_type = models.CharField(_("job type"), max_length=20, choices=JobTypeEnum.choices)
    status = models.CharField(_("status"), max_length=20, choices=JobStatusEnum.choices)
    state = models.CharField(
        _("state"),
        max_length=20,
        choices=JobStateEnum.choices,
        default=JobStateEnum.ONGOING,
        null=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        to=JobCategory, related_name="job_template", blank=True
    )
    documents = models.ManyToManyField(
        to=DocumentTemplate, related_name="job_template", blank=True
    )
    notes = models.ManyToManyField(
        to=NoteTemplate, related_name="job_template", blank=True
    )
    tasks = models.ManyToManyField(
        to=TaskTemplate, related_name="job_template", blank=True
    )
