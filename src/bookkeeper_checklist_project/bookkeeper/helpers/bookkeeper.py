from bookkeeper.models import Bookkeeper
import traceback
from core.utils import ProjectError, get_formatted_logger, debugging_print
from django.db.models import QuerySet
from jobs.models import Job
from client.models import Client

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
