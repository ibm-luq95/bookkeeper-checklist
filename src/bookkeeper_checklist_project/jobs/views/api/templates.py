# -*- coding: utf-8 -*-#
import traceback

from django.contrib import messages
from django.db import transaction
from django.urls import reverse_lazy
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from rest_framework import status
from django.core import serializers
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from bookkeeper.models import BookkeeperProxy
from client.models import ClientProxy
from core.api.permissions import BaseApiPermissionMixin
from core.utils import get_formatted_logger, debugging_print, get_trans_txt
from documents.models import Documents
from jobs.models import JobTemplate, Job, JobProxy
from notes.models import Note
from task.models import Task
from jobs.serializers import JobTemplateSerializer, JobSerializer, JobOnlySerializer

logger = get_formatted_logger()


class JobRetrieveTemplateApi(RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        BaseApiPermissionMixin,
    )
    perm_slug = "jobs.jobtemplate"
    queryset = JobTemplate.objects.all()
    serializer_class = JobTemplateSerializer


class CreateNewJobFromTemplateApi(APIView):
    permission_classes = (permissions.IsAuthenticated, BaseApiPermissionMixin)

    perm_slug = "jobs.jobtemplate"

    def post(self, request: Request, *args, **kwargs):
        try:
            data = request.data
            template_pk = data.get("templatePk")
            returned_data = dict()
            selectedOption = data.get("selectedOption")
            clients = data.get("clients", None)
            templateManager = data.get("templateManager", None)
            debugging_print(data)

            # raise Exception("Stop")
            with transaction.atomic():
                # if selectedOption == "create_job":
                template_obj = JobTemplate.objects.select_related().get(pk=template_pk)
                job_categories = template_obj.categories.all()
                tasks = template_obj.tasks.all()
                notes = template_obj.notes.all()
                documents = template_obj.documents.all()
                new_job_data = {
                    "title": f"Copy - {template_obj.title}",
                    "description": template_obj.description,
                    "job_type": template_obj.job_type,
                    "status": template_obj.status,
                    "is_created_from_template": True,
                    # "due_date": template_obj.due_date,
                }
                if templateManager:
                    bookkeeper = BookkeeperProxy.objects.get(pk=templateManager)
                    new_job_data.update({"managed_by": bookkeeper.user})
                new_job = JobProxy.objects.create(**new_job_data)
                if job_categories:
                    debugging_print(job_categories)
                    # raise APIException("Stop")
                    for category in job_categories:
                        new_job.categories.add(category)
                    new_job.save()
                returned_data["msg"] = get_trans_txt(f"Job created successfully!")
                # returned_data["job_object"] = JobSerializer(instance=new_job).data

                # returned_data["job_object"] = serializers.serialize("json", new_job)
                returned_data["job_url"] = reverse_lazy(
                    "jobs:update", kwargs={"pk": new_job.pk}
                )
                messages.success(self.request, returned_data["msg"])
                if tasks:
                    for task in tasks:
                        task_data = {
                            "title": task.title,
                            "task_type": task.task_type,
                            "additional_notes": task.notes,
                            "status": task.status,
                            "job": new_job,
                        }
                        task_object = Task.objects.create(**task_data)
                        if task.items.all():
                            task_items = []
                            for item in task.items.all():
                                task_items.append(item)
                            task_object.items.add(*task_items)
                            task_object.save()

                if notes:
                    for note in notes:
                        note_data = {
                            "title": note.title,
                            "body": note.body,
                            "job": new_job,
                            "note_section": "job",
                        }
                        Note.objects.create(**note_data)
                if documents:
                    for document in documents:
                        document_data = {
                            "title": document.title,
                            "document_section": "job",
                            "job": new_job,
                            "document_file": document.template_file,
                        }
                        Documents.objects.create(**document_data)

                if clients:
                    for client in clients:
                        client_obj = (
                            ClientProxy.objects.select_related().filter(pk=client).first()
                        )
                        if not client_obj:
                            raise APIException(
                                get_trans_txt(f"Client {client} not exists!")
                            )
                        new_job.pk = None
                        new_job.id = None
                        new_job._state.adding = True
                        new_job.client = client_obj
                        new_job.save()

                # else:
                #     debugging_print("NNNNNNNNNNNNNNNNNNNN")
                #     raise Exception("no clients")

                # debugging_print(tasks)
                # debugging_print(documents)
                # debugging_print(notes)
                # debugging_print(job_categories)

                # debugging_print(new_job_data)
                # this to check if the job exists with the same title
                # check_job_exists = Job.objects.filter(title=new_job_data.get("title"))
                # debugging_print(check_job_exists)
                # raise APIException()

                debugging_print(new_job.tasks.all())
                debugging_print(new_job.documents.all())
                # debugging_print(new_job.get_instance_as_dict)
                # returned_data["job_object"] = new_job.get_instance_as_dict
                # returned_data["job_object"] = serializers.serialize("json", [new_job])
                # returned_data["job_object"] = JobOnlySerializer(instance=new_job).data
                # debugging_print(returned_data["job_object"])

            return Response(
                data=returned_data,
                status=status.HTTP_201_CREATED,
            )
        except APIException as ex:
            # logger.error("API Exception")
            # logger.error(serializer.errors)
            logger.error(ex)
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "user_error_msg": ex.detail,
                # "user_error_msg": serializer.errors,
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            # debugging_print(ex)
            logger.error(traceback.format_exc())
            response_data = {
                "status": status.HTTP_400_BAD_REQUEST,
                "error": str(ex),
                "user_error_msg": "Error while create job!",
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
