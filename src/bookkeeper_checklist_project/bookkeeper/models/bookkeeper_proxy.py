# -*- coding: utf-8 -*-#
from bookkeeper.models import Bookkeeper


class BookkeeperProxy(Bookkeeper):
    class Meta:
        proxy = True

    def get_tasks_count(self):
        all_tasks = []
        all_jobs = self.user.jobs.all()
        if all_jobs:
            for job in all_jobs:
                all_tasks.append(job.tasks.count())
        return sum(all_tasks)

    @property
    def get_clients_total(self) -> int:
        total_list = set()
        jobs = self.jobs.all()
        if jobs:
            for job in jobs:
                total_list.add(str(job.client.pk))
        return len(total_list)

    def get_tasks(self) -> list:
        all_lists = []
        all_jobs = self.user.jobs.all()
        if all_jobs:
            for job in all_jobs:
                tasks = job.tasks.all()
                if tasks:
                    for task in tasks:
                        all_lists.append(task)
        return all_lists
