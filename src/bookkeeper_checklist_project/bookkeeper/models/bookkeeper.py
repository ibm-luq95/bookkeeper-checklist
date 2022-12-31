from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

from client.models import Client
from company_services.models import CompanyService
from core.choices import CustomUserStatusEnum
from core.models import BaseModelMixin, UserForeignKeyMixin
from core.utils import debugging_print


# from jobs.models import Job


class Bookkeeper(BaseModelMixin, UserForeignKeyMixin):
    """Bookkeeper model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    slug = models.SlugField(_("slug"), max_length=250, null=True, blank=True)
    profile_picture = models.ImageField(
        _("profile_picture"), upload_to="profile_pictures/", null=True, blank=True
    )
    status = models.CharField(
        _("status"),
        max_length=10,
        choices=CustomUserStatusEnum.choices,
        default=CustomUserStatusEnum.ENABLED,
    )
    company_services = models.ForeignKey(
        to=CompanyService,
        on_delete=models.PROTECT,
        null=True,
        related_name="bookkeeper",
    )
    # clients = models.ManyToManyField(to=Client)
    is_active = models.BooleanField(_("is_active"), default=True)
    bio = models.TextField(_("bio"), null=True, blank=True)

    def __str__(self) -> str:
        return f"Bookkeeper - {self.user.first_name} {self.user.last_name}"

    class Meta(BaseModelMixin.Meta):
        permissions = [
            ("bookkeeper_user", "Bookkeeper User"),
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.fullname)
        super(Bookkeeper, self).save(*args, **kwargs)

    def get_tasks_count(self):
        all_tasks = []
        all_jobs = self.jobs.all()
        for job in all_jobs:
            all_tasks.append(job.tasks.count())
        return sum(all_tasks)

    @property
    def is_active_labeled(self) -> str:
        if self.is_active is True:
            return "Active"
        else:
            return "Deactivate"

    @property
    def get_clients_total(self) -> int:
        total_list = set()
        jobs = self.jobs.select_related()
        for job in jobs:
            total_list.add(str(job.client.pk))
        return len(total_list)
