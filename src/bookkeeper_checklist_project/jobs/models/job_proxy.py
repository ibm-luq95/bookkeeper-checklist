# -*- coding: utf-8 -*-#
from django.db import transaction
from django.db.models import Q

from core.constants.status_labels import (
    CON_ARCHIVED,
    CON_COMPLETED,
    CON_ENABLED,
    CON_NOT_STARTED,
)
from jobs.models import Job


class JobProxy(Job):
    class Meta:
        proxy = True

    def unplug_bookkeeper_for_client_finished_job(self):
        managed_by = self.managed_by
        if self.status == CON_COMPLETED or self.status == CON_ARCHIVED:
            if managed_by:
                with transaction.atomic():
                    client = self.client
                    bookkeeper_obj = managed_by.bookkeeper
                    client.bookkeepers.remove(bookkeeper_obj)
                    client.save()
                    # debugging_print(self.model_class())
                    JobProxy.objects.filter(pk=self.pk).update(managed_by=None)

    def archive_and_unarchived_related_items(self, status: str) -> None:
        with transaction.atomic():
            documents = self.documents.all()
            tasks = self.tasks.all()
            notes = self.notes.all()
            if status == CON_ARCHIVED or status == CON_COMPLETED:
                if notes:
                    notes.update(status=CON_ARCHIVED)
                # Set documents to archived
                if documents:
                    documents.update(status=CON_ARCHIVED)
                    # Set tasks to archived
                if tasks:
                    tasks.update(status=CON_ARCHIVED)
            else:
                # Set notes to enabled
                if notes:
                    notes.filter(Q(status=CON_ARCHIVED)).update(status=CON_ENABLED)
                # # Set documents to enabled
                if documents:
                    documents.filter(Q(status=CON_ARCHIVED)).update(status=CON_ENABLED)
                # Set tasks to archived
                if tasks:
                    tasks.filter(Q(status=CON_ARCHIVED)).update(status=CON_NOT_STARTED)