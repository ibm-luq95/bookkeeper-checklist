# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin, CreatedByMixin, StrModelMixin


class NoteTemplate(BaseModelMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=60, null=False)
    body = models.TextField(_("body"), null=False)
