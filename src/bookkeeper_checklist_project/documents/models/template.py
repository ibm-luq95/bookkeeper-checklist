# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin, StrModelMixin


class DocumentTemplate(BaseModelMixin, StrModelMixin):
    title = models.CharField(_("title"), max_length=50)
    template_file = models.FileField(_("template file"), upload_to="document_templates/")
