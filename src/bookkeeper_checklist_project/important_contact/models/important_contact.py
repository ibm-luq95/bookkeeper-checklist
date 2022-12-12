from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from core.models import BaseModelMixin


class ImportantContact(BaseModelMixin):
    """Important contact for client

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    company_name = models.CharField(_("company name"), max_length=60, null=True, blank=True)
    contact_label = models.CharField(_("label"), max_length=50, null=False)
    contact_description = models.TextField(_("description"), null=True, blank=True)
    contact_first_name = models.CharField(_("first name"), max_length=50, null=False)
    contact_last_name = models.CharField(_("last name"), max_length=50, null=False)
    contact_email = models.EmailField(_("contact email"), null=False)
    contact_city = models.CharField(_("city"), max_length=50, null=True, blank=True)
    contact_state = models.CharField(_("state"), max_length=50, null=True, blank=True)
    contact_postcode = models.CharField(_("postcode"), max_length=50, null=True, blank=True)
    contact_phone = models.CharField(_("phone"), max_length=80, null=False, blank=True)
    contact_website = models.URLField(_("website"), null=True, blank=True)
    contact_notes = models.TextField(_("notes"), null=True, blank=True)

    def get_absolute_url(self):
        return reverse("manager:client_account:details", kwargs={"pk": self.pk})

    @property
    def contact_fullname(self):
        return f"{self.contact_first_name} {self.contact_last_name}"
