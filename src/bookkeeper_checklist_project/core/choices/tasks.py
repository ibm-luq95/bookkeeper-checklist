# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class TaskStatusEnum(models.TextChoices):
    NO_TYPE = "no_type", _("No Type")
    RECURRING = "recurring", _("Recurring")
    WEEKLY = "weekly", _("Weekly")
    MONTHLY = "monthly", _("Monthly")
    QUARTERLY = "quarterly", _("Quarterly")
    YEARLY = "yearly", _("Yearly")
    ONE_TIME = "one_time", _("One Time")
    URGENT = "urgent", _("Urgent")


class TaskTypeEnum(models.TextChoices):
    NO_TYPE = "no_type", _("No Type")
    RECURRING = "recurring", _("Recurring")
    WEEKLY = "weekly", _("Weekly")
    MONTHLY = "monthly", _("Monthly")
    QUARTERLY = "quarterly", _("Quarterly")
    YEARLY = "yearly", _("Yearly")
    ONE_TIME = "one_time", _("One Time")
    URGENT = "urgent", _("Urgent")