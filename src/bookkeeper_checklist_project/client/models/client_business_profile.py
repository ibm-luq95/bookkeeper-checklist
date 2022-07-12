from core.models import BaseModelMixin
from django.db import models
from django.utils.translation import gettext as _


class ClientBusinessProfile(BaseModelMixin):
    phone = models.CharField(_("phone"), max_length=50, null=True)
    website_url = models.URLField(_("website_url"), max_length=50, null=True)
    address = models.CharField(_("address"), max_length=50, null=True)
    contact = models.CharField(_("contact"), max_length=50, null=True)
