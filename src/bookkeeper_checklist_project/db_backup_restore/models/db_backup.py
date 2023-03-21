# -*- coding: utf-8 -*-#
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin, GeneralStatusFieldMixin
from core.models.slugify_mixin import SlugifyMixin


class DBBackup(BaseModelMixin, SlugifyMixin, GeneralStatusFieldMixin):
    name = models.CharField(_("backup name"), max_length=100)
    backup_path = models.FileField(
        _("backup path"),
        editable=False,
        null=True,
        blank=True,
        upload_to=settings.BASE_DIR / "db_backups",
    )
    is_restored = models.BooleanField(_("restored"), default=False, editable=False)
    restored_at = models.DateTimeField(
        _("restored at"), editable=False, null=True, blank=True
    )
