from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

from client.models import Client
from company_services.models import CompanyService
from core.choices import CustomUserStatusEnum
from core.models import BaseModelMixin, UserForeignKeyMixin
from core.models import StaffMemberMixin
from core.utils import debugging_print


# from jobs.models import Job


class Bookkeeper(StaffMemberMixin):
    """Bookkeeper model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    class Meta(StaffMemberMixin.Meta):
        # proxy = True
        permissions = [
            ("bookkeeper_user", "Bookkeeper User"),
        ]

    def __str__(self):
        return f"Bookkeeper -> {self.user.fullname}"

    def get_tasks_count(self):
        all_tasks = []
        all_jobs = self.jobs.all()
        for job in all_jobs:
            all_tasks.append(job.tasks.count())
        return sum(all_tasks)

    @property
    def get_clients_total(self) -> int:
        total_list = set()
        jobs = self.jobs.select_related()
        for job in jobs:
            total_list.add(str(job.client.pk))
        return len(total_list)
