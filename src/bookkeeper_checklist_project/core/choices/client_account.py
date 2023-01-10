# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _


class ClientAccountStatusEnum(models.TextChoices):
    ENABLED = "enabled", _("Enabled")
    DISABLED = "disabled", _("Disabled")
    ARCHIVE = "archive", _("Archive")
