from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin
from . import ClientAccount, ImportantContact


class Client(BaseModelMixin):
    """This is client model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    name = models.CharField(_("name"), max_length=50, null=True)
    email = models.EmailField(_("email"), max_length=50, null=True)
    industry = models.CharField(_("industry"), max_length=50, null=True)
    client_account = models.ForeignKey(
        to=ClientAccount,
        on_delete=models.PROTECT,
        null=True,
        related_name="client",
        blank=True,
    )
    important_contact = models.OneToOneField(
        to=ImportantContact,
        on_delete=models.PROTECT,
        null=True,
        related_name="client",
        blank=True,
    )
    is_active = models.BooleanField(_("is_active"), default=True)
    company_logo = models.ImageField(
        _("company_logo"), upload_to="logos/", null=True, blank=True
    )

    def __str__(self) -> str:
        # return self.client_account
        # return f"{self.email} - {self.client_account}"
        return self.name
