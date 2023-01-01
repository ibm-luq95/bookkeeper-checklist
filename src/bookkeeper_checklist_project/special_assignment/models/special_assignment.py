# -*- coding: utf-8 -*-#
from typing import Union

from django.db import models
from django.utils.translation import gettext as _

from assistant.models import Assistant
from bookkeeper.models import Bookkeeper
from client.models import Client
from core.choices.special_assignment import SpecialAssignmentStatusEnum
from core.models import BaseModelMixin, UserForeignKeyMixin
from manager.models import Manager


class SpecialAssignment(BaseModelMixin):
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
    assistant = models.ForeignKey(
        to=Assistant,
        on_delete=models.PROTECT,
        related_name="special_assignments",
        null=True,
        blank=True,
    )
    bookkeeper = models.ForeignKey(
        to=Bookkeeper,
        on_delete=models.PROTECT,
        related_name="special_assignments",
        null=True,
        blank=True,
    )
    manager = models.ForeignKey(
        to=Manager,
        on_delete=models.PROTECT,
        related_name="special_assignments",
        null=True,
        blank=True,
    )

    def get_managed_user(self) -> Union[Bookkeeper, Assistant, Manager, None]:
        if self.bookkeeper:
            return self.bookkeeper
        elif self.assistant:
            return self.assistant
        elif self.manager:
            return self.manager
        else:
            return None

    def get_is_seen_label(self) -> str:
        if self.is_seen is True:
            return "Seen"
        else:
            return "Not seen"
