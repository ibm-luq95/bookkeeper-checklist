# -*- coding: utf-8 -*-#
from typing import Union

from django.db import models
from django.utils.translation import gettext as _


from client.models import Client
from core.choices.special_assignment import SpecialAssignmentStatusEnum
from core.models import BaseModelMixin, TeamMembersMixin
from .managers import SpecialAssignmentsManager


class SpecialAssignment(BaseModelMixin, TeamMembersMixin):
    client = models.ForeignKey(
        to=Client, on_delete=models.PROTECT, related_name="special_assignments"
    )
    title = models.CharField(_("title"), max_length=70, null=False, blank=False)
    body = models.TextField(_("body"))
    status = models.CharField(
        _("status"),
        max_length=15,
        choices=SpecialAssignmentStatusEnum.choices,
        default=SpecialAssignmentStatusEnum.NOT_STARTED,
    )
    attachment = models.FileField(
        _("attachment"), upload_to="special_assignment_attachments/", null=True, blank=True
    )
    start_date = models.DateField(_("start date"))
    due_date = models.DateField(_("due date"))
    notes = models.TextField(_("notes"), null=True, blank=True)
    is_seen = models.BooleanField(_("is_seen"), default=False)

    objects = SpecialAssignmentsManager()

    def __str__(self) -> str:
        return f"{self.title}"

    def get_is_seen_label(self) -> str:
        if self.is_seen is True:
            return "Seen"
        else:
            return "Not seen"