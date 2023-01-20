# -*- coding: utf-8 -*-#

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from client.models import Client
from core.choices.special_assignment import SpecialAssignmentStatusEnum
from core.models import BaseModelMixin, TeamMembersMixin
from core.utils import get_trans_txt
from core.utils import FileValidator
from .managers import SpecialAssignmentsManager

file_validator = FileValidator(
    max_size=1024 * 1000,
    content_types=(
        "image/png",
        "image/jpeg",
        "text/csv",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/vnd.oasis.opendocument.spreadsheet",
        "application/pdf",
        "text/plain",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.oasis.opendocument.text",
    ),
)


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
        _("attachment"),
        upload_to="special_assignment_attachments/",
        null=True,
        blank=True,
        validators=[file_validator],
    )
    start_date = models.DateField(_("start date"))
    due_date = models.DateField(_("due date"))
    notes = models.TextField(_("notes"), null=True, blank=True)
    is_seen = models.BooleanField(_("is_seen"), default=False)
    assigned_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="requested_assignments",
        help_text=_("readonly, you cant modified it"),
    )

    objects = SpecialAssignmentsManager()

    class Meta(BaseModelMixin.Meta):
        permissions = (
            (
                "bookkeeper_can_delete_special_assignment",
                "Bookkeeper can delete special assignment",
            ),
        )

    def __str__(self) -> str:
        return f"{self.title}"

    def get_is_seen_label(self) -> str:
        if self.is_seen is True:
            return get_trans_txt("Seen")
        else:
            return get_trans_txt("Not seen")
