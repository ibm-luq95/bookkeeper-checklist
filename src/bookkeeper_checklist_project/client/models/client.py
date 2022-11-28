from PIL import Image
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from core.models import BaseModelMixin
from important_contact.models import ImportantContact


class Client(BaseModelMixin):
    """This is client model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    important_contact = models.OneToOneField(
        to=ImportantContact,
        on_delete=models.RESTRICT,
        null=True,
        related_name="client",
        blank=True,
    )
    name = models.CharField(_("name"), max_length=50, null=True)
    email = models.EmailField(_("email"), max_length=50, null=True)
    industry = models.CharField(_("industry"), max_length=50, null=True)
    is_active = models.BooleanField(_("is_active"), default=True)
    company_logo = models.ImageField(
        _("company_logo"),
        upload_to="logos/",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        # return self.client_account
        # return f"{self.email} - {self.client_account}"
        return self.name

    def save(self, *args, **kwargs):
        super(Client, self).save(*args, **kwargs)
        if self.company_logo:
            image = Image.open(self.company_logo.path)
            if image.height > 150 or image.width > 150:
                output_size = (150, 150)
                image.thumbnail(output_size)
                image.save(self.company_logo.path)

    def get_absolute_url(self):
        return reverse("manager:client:details", kwargs={"pk": self.pk})

    def get_tasks_count(self):
        return self.jobs.all()
