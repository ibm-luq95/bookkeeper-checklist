from core.choices import AccountType
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _

from . import BankUserAccount


class BankAccountItem(BaseModelMixin):
    """Bank account item for every bank user account

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    label = models.CharField(_("label"), max_length=30)
    bank_account_type = models.CharField(
        _("bank_account_type"), max_length=50, choices=AccountType.choices
    )
    bank_user_account = models.ManyToManyField(to=BankUserAccount)
