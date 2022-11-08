from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class ClientAccount(BaseModelMixin):
    """Client account model related with client

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    account_name = models.CharField(_("account name"), max_length=50, null=True)
    account_email = models.EmailField(_("account email"), max_length=50, null=True)
    account_url = models.URLField(_("account url"), max_length=50, null=True)
    account_username = models.CharField(_("account username"), max_length=30, null=True)
    account_password = models.CharField(
        _("account password"), max_length=250, null=True
    )
    last_modified_date = models.DateTimeField(_("last_modified_date"), auto_now=True)

    def __str__(self) -> str:
        return f"{self.account_name}"
