import traceback

from django.utils import timezone

from bookkeeper.models import Bookkeeper
from client.models import Client
from core.models import BaseQuerySetMixin
from core.utils import ProjectError, get_formatted_logger
from jobs.models import Job

logger = get_formatted_logger(__file__)


class BookkeeperHelper:
    def __init__(self, bookkeeper: Bookkeeper):
        self.bookkeeper = bookkeeper

    @property
    def get_tasks_total_count(self) -> int:
        """Retrieve total count of tasks for bookkeeper

        Args:
            self: bookkeeper instance
        Raises:
            ProjectError: If any exception occurred
            Exception: Any exception will occur will return None

        Returns:
            int: Integer number of total tasks for specific bookkeeper
            None: If any exception occurred
        """
        try:
            tasks_total_count = []
            for job in self.bookkeeper.jobs.all():
                tasks_total_count.append(job.tasks.count())

            return sum(tasks_total_count)
        except ProjectError as ex:
            logger.error(traceback.format_exc())
            raise Exception(ex.message)
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))

    def get_clients(self) -> BaseQuerySetMixin:
        """Retrieve all clients handled by bookkeeper

        Args:
            self: bookkeeper instance
        Raises:
            ProjectError: If any exception occurred
            Exception: Any exception will occur will return None

        Returns:
            BaseQuerySetMixin: QuerySet of all clients
            None: If any exception occurred
        """
        try:
            jobs = Job.objects.all()
            jobs_queryset = jobs.filter(bookkeeper=self.bookkeeper).values_list("client")
            jobs_queryset = [pk[0] for pk in jobs_queryset]
            queryset = Client.objects.filter(pk__in=jobs_queryset)
            return queryset
        except ProjectError as ex:
            logger.error(traceback.format_exc())
            raise Exception(ex.message)
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))

    @property
    def get_past_due_tasks_total(self) -> int:
        """Retrieve total count of past due tasks

        Args:
            self: bookkeeper instance
        Raises:
            ProjectError: If any exception occurred
            Exception: Any exception will occur will return None

        Returns:
            int: total number of past due tasks
            None: If any exception occurred
        """
        try:
            past_due_tasks_list = []
            jobs = Job.objects.all()
            jobs_queryset = jobs.filter(bookkeeper=self.bookkeeper)
            for job in jobs_queryset:
                for task in job.tasks.all():
                    now = timezone.now().date()
                    # debugging_print(task.due_date)
                    if now > task.due_date:
                        past_due_tasks_list.append(task)
            return len(past_due_tasks_list)
        except ProjectError as ex:
            logger.error(traceback.format_exc())
            raise Exception(ex.message)
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))

    def get_last_tasks(self, task_limit: int = 10) -> list:
        """Retrieve last tasks for bookkeeper

        Args:
            self: bookkeeper instance
            task_limit: int limit of last tasks
        Raises:
            ProjectError: If any exception occurred
            Exception: Any exception will occur will return None

        Returns:
            list: List of last tasks
            None: If any exception occurred
        """
        try:
            tasks_list = []
            all_jobs = self.bookkeeper.jobs.all()
            for job in all_jobs:
                # debugging_print(job.title)
                if job.tasks.filter():
                    for task in job.tasks.filter():
                        if len(tasks_list) <= task_limit:
                            tasks_list.append(task)
            return tasks_list
        except ProjectError as ex:
            logger.error(traceback.format_exc())
            raise Exception(ex.message)
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))
