from distutils.command import upload
from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _

from . import ClientAccount, ClientBusinessProfile


class Client(BaseModelMixin):
    name = models.CharField(_("name"), max_length=50, null=True)
    email = models.EmailField(_("email"), max_length=50, null=True)
    industry = models.CharField(_("industry"), max_length=50, null=True)
    client_account = models.ForeignKey(
        to=ClientAccount, on_delete=models.PROTECT, null=True, related_name="client"
    )
    business_profile = models.OneToOneField(
        to=ClientBusinessProfile,
        on_delete=models.PROTECT,
        null=True,
        related_name="client",
    )
    is_active = models.BooleanField(_("is_active"), default=True)
    company_logo = models.ImageField(_("company_logo"), upload_to="logos/", null=True)
