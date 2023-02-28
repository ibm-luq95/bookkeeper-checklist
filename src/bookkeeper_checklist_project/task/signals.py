# -*- coding: utf-8 -*-#
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from core.constants.status_labels import CON_COMPLETED, CON_NOT_COMPLETED
from task.models import Task


@receiver(post_save, sender=Task)
def update_job_status_when_add_task(sender, instance: Task, created, **kwargs):
    with transaction.atomic():
        # if created:
        created_task_obj = instance
        job_object = created_task_obj.job
        if job_object:
            not_completed_tasks = job_object.get_all_not_completed_tasks()
            if len(not_completed_tasks) > 0:
                job_object.status = CON_NOT_COMPLETED
            else:
                job_object.status = CON_COMPLETED
            job_object.save()
        # else:
        #     debugging_print("Update task")
