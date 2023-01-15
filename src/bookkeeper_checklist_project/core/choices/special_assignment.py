# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class SpecialAssignmentStatusEnum(models.TextChoices):
    NOT_STARTED = "not_started", _("Not Started")
    IN_PROGRESS = "in_progress", _("In Progress")
    COMPLETED = "completed", _("Completed")
    REJECTED = "rejected", _("Rejected")
    ARCHIVE = "archive", _("Archive")
