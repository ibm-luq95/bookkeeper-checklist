from django.db import models
from django.utils.translation import gettext as _

from core.models import BaseModelMixin


class ImportantContact(BaseModelMixin):
    """Important contact for client

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    company_name = models.CharField(
        _("company name"), max_length=60, null=True, blank=True
    )
    description = models.TextField(_("description"), null=True, blank=True)
    first_name = models.CharField(_("first name"), max_length=50, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, null=True, blank=True)
    email = models.EmailField(_("email"), null=True, blank=True)
    city = models.CharField(_("city"), max_length=50, null=True, blank=True)
    street_address = models.CharField(
        _("street address"), max_length=50, null=True, blank=True
    )
    state = models.CharField(_("state"), max_length=50, null=True, blank=True)
    postcode = models.CharField(_("postcode"), max_length=50, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=80, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True)
