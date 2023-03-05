# -*- coding: utf-8 -*-#
from django.db import transaction
from django.db.models.signals import post_save

from jobs.models import JobProxy


# @receiver(post_save, sender=Job)
def unplug_bookkeeper_for_completed_job(
    sender, instance: JobProxy, created: bool, **kwargs
):
    if not created:
        with transaction.atomic():
            job_object = instance
            if job_object.status != job_object.get_changed_columns().get("status"):
                job_object.unplug_bookkeeper_for_client_finished_job()
                job_object.archive_and_unarchived_related_items(job_object.status)


post_save.connect(unplug_bookkeeper_for_completed_job, sender=JobProxy)
