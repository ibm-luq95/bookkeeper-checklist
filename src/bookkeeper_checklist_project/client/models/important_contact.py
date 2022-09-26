from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class ImportantContact(BaseModelMixin):
    """Important contact for client

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    contact_fields = models.JSONField(
        _("contact_fields"), default=dict, null=True, blank=True
    )
