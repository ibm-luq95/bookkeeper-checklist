# -*- coding: utf-8 -*-#
import textwrap
from typing import Union

from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin, TeamMembersMixin
from .managers import RepliesManager
from .special_assignment import SpecialAssignment


class Discussion(BaseModelMixin, TeamMembersMixin):
    special_assignment = models.ForeignKey(
        to=SpecialAssignment,
        on_delete=models.CASCADE,
        related_name="discussions",
        null=True,
        blank=True,
    )
    title = models.CharField(_("title"), max_length=100, null=True, blank=True)
    body = models.TextField(_("body"))
    replies = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        related_name="discussion_replies",
        null=True,
        blank=True,
        help_text=_("Optional, This will use when you want to reply on custom reply"),
    )
    attachment = models.FileField(
        _("attachment"), upload_to="discussion_attachment/", null=True, blank=True
    )
    is_seen = models.BooleanField(_("is_seen"), default=False)

    objects = RepliesManager()

    def __str__(self) -> str:
        # return self.title
        return textwrap.shorten(self.body, width=40, placeholder="...")
