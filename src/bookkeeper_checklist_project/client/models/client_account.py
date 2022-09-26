from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class ClientAccount(BaseModelMixin):
    """Client account model related with client

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    account_name = models.CharField(_("account_name"), max_length=50, null=True)
    account_email = models.EmailField(_("account_email"), max_length=50, null=True)
    account_url = models.URLField(_("account_url"), max_length=50, null=True)
    account_username = models.CharField(_("account_username"), max_length=30, null=True)
    account_password = models.CharField(
        _("account_password"), max_length=250, null=True
    )
    last_modified_date = models.DateTimeField(_("last_modified_date"), auto_now=True)
