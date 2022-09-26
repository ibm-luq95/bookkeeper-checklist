from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class BankProfile(BaseModelMixin):
    """Bank profile model for every bank user account

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    bank_name = models.CharField(_("bank_name"), max_length=30)
    bank_url = models.URLField(_("bank_url"))
    bank_login_url = models.URLField(_("bank_login_url"))
    bank_tech_support_url = models.URLField(_("bank_tech_support_url"), null=True)
