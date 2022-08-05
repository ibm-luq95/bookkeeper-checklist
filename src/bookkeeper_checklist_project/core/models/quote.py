from .mixins import BaseModelMixin
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Quote(BaseModelMixin):
    full_quote_object = models.JSONField(_("full_quote_object"))
    quote_text = models.TextField(_("quote_text"))
    quote_choice = models.CharField(_("quote_choice"), max_length=20)
    author = models.CharField(_("author"), max_length=60, null=True)
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta(BaseModelMixin.Meta):
        indexes = [models.Index(fields=["created_at"])]
