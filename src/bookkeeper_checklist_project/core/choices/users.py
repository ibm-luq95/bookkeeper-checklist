# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class CustomUserTypeEnum(models.TextChoices):
    BOOKKEEPER = "bookkeeper", _("Bookkeeper")
    ASSISTANT = "assistant", _("Assistant")
    MANAGER = "manager", _("Manager")


class CustomUserStatusEnum(models.TextChoices):
    ENABLED = "enabled", _("Enabled")
    PENDING = "pending", _("Pending")
    CANCELED = "canceled", _("Canceled")
    DISABLED = "disabled", _("Disabled")
    ARCHIVE = "archive", _("Archive")
