# -*- coding: utf-8 -*-#
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.constants.status_labels import CON_COMPLETED
from jobs.models import Job


@receiver(post_save, sender=Job)
def unplug_bookkeeper_for_completed_job(sender, instance: Job, created, **kwargs):
    if not created:
        with transaction.atomic():
            job_object = instance
            if job_object.status == CON_COMPLETED:
                client_object = instance.client
                job_managed_by = job_object.managed_by
                bookkeeper_obj = job_managed_by.bookkeeper
                client_object.bookkeepers.remove(bookkeeper_obj)
                client_object.save()
