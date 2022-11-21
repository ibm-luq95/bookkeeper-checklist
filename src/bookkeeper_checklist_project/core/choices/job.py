# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class JobTypeEnum(models.TextChoices):
    NO_TYPE = "no_type", _("No Type")
    RECURRING = "recurring", _("Recurring")
    WEEKLY = "weekly", _("Weekly")
    MONTHLY = "monthly", _("Monthly")
    QUARTERLY = "quarterly", _("Quarterly")
    YEARLY = "yearly", _("Yearly")
    ONE_TIME = "one_time", _("One Time")
    URGENT = "urgent", _("Urgent")


class JobStatusEnum(models.TextChoices):
    NOT_STARTED = "not_started", _("Not Started")
    IN_PROGRESS = "in_progress", _("In Progress")
    PAST_DUE = "past_due", _("Past Due")
    COMPLETE = "complete", _("Complete")
    ARCHIVE = "archive", _("Archive")