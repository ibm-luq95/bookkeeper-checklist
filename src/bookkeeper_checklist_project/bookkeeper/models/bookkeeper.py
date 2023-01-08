from django.db import models
from django.utils.translation import gettext as _


from core.models import BaseModelMixin, StaffMemberMixin


class Bookkeeper(BaseModelMixin, StaffMemberMixin):
    """Bookkeeper model

    Args:
        BaseModelMixin (models.Model): Django base model mixin
    """

    class Meta:
        # proxy = True
        permissions = [
            ("bookkeeper_user", "Bookkeeper User"),
        ]

    def __str__(self):
        # return f"Bookkeeper -> {self.user.fullname}"
        return f"{self.user.fullname}"

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

