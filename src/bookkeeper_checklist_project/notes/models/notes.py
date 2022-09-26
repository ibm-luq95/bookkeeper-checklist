from client.models import Client
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class Note(BaseModelMixin):
    """Notes model for bookkeeper, assistant, and manager

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    title = models.CharField(_("title"), max_length=60, null=False)
    body = models.TextField(_("body"), null=False)
    client = models.ForeignKey(to=Client, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "notes"
