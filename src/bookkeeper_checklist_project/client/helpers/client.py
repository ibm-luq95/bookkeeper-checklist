# -*- coding: utf-8 -*-#
import traceback

from core.utils import ProjectError, get_formatted_logger

logger = get_formatted_logger(__file__)


class ClientHelper:
    @staticmethod
    def get_tasks_total_count_for_all_jobs(client) -> int:
        """Retrieve total count of tasks for all jobs

        Args:
            client: bookkeeper instance
        Raises:
            ProjectError: If any exception occurred
            Exception: Any exception will occur will return None

        Returns:
            int: Integer number of total tasks for all jobs
            None: If any exception occurred
        """
        try:

            return 0
        except ProjectError as ex:
            logger.error(traceback.format_exc())
            raise Exception(ex.message)
        except Exception as ex:
            logger.error(traceback.format_exc())
            raise Exception(str(ex))
