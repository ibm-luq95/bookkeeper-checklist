from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _
from . import BankUserAccount


class AccountType(models.TextChoices):
    CHECKING_ACCOUNT = "checking_account", _("Checking Account")
    SAVING_ACCOUNT = "saving_account", _("Saving Account")
    CREDITCARD = "credit_card", _("CreditCard")
    LOAN = "loan", _("Loan")


class BankAccountItem(BaseModelMixin):
    label = models.CharField(_("label"), max_length=30)
    bank_account_type = models.CharField(
        _("bank_account_type"), max_length=50, choices=AccountType.choices
    )
    bank_user_account = models.ManyToManyField(to=BankUserAccount)
