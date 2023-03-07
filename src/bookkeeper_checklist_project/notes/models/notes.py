from django.db import models
from django.utils.translation import gettext as _

from client.models import ClientProxy
from core.choices import NoteTypesEnum
from core.models import (
    BaseModelMixin,
    CreatedByMixin,
    GetObjectSectionMixin,
    GeneralStatusFieldMixin,
)
from jobs.models import Job
from task.models import Task


class Note(BaseModelMixin, CreatedByMixin, GetObjectSectionMixin, GeneralStatusFieldMixin):
    """Notes model for bookkeeper, assistant, and manager

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    title = models.CharField(_("title"), max_length=60, null=False)
    body = models.TextField(_("body"), null=False)
    client = models.ForeignKey(
        to=ClientProxy,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notes",
    )
    job = models.ForeignKey(
        to=Job, on_delete=models.SET_NULL, null=True, blank=True, related_name="notes"
    )
    task = models.ForeignKey(
        to=Task, on_delete=models.SET_NULL, null=True, blank=True, related_name="notes"
    )
    note_section = models.CharField(
        _("note section"),
        max_length=15,
        null=True,
        blank=True,
        choices=NoteTypesEnum.choices,
    )

    class Meta(BaseModelMixin.Meta):
        verbose_name_plural = "notes"

    def __str__(self):
        return f"{self.title}"
