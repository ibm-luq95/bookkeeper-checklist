from client.models import Client
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _

from . import BankProfile


class BankUserAccount(BaseModelMixin):
    """Bank user account model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    clients = models.ManyToManyField(to=Client)
    bank_profile = models.ForeignKey(
        to=BankProfile, on_delete=models.PROTECT, related_name="bank_user_account"
    )
    username = models.CharField(_("username"), max_length=30, null=True)
    password = models.CharField(_("password"), max_length=250, null=True)
    status = models.BooleanField(_("status"), null=True)
