# -*- coding: utf-8 -*-#
from rest_framework import serializers
from django.db import transaction
from core.utils.developments import debugging_print
from jobs.models import JobTemplate
from notes.models import NoteTemplate
from documents.models import DocumentTemplate
from task.models import TaskTemplate


class SaveRelatedJobTemplateSerializer(serializers.BaseSerializer):
    job_template = serializers.PrimaryKeyRelatedField(
        queryset=JobTemplate.objects.all(), many=True
    )

    def create(self, validated_data: dict):
        # debugging_print(locals())
        # debugging_print(self.Meta.model._meta.object_name)
        # debugging_print(self.Meta.model)
        # self.Meta.model.get_fields_as_list
        with transaction.atomic():
            job_template_obj = validated_data.pop(
                "job_template"
            )  # removing job_template from validated_data
            instance = None
            job_template_obj = job_template_obj[0]
            match self.Meta.model._meta.object_name:  # type: ignore
                case "NoteTemplate":
                    instance = NoteTemplate.objects.create(
                        **validated_data
                    )  # saving note template object
                    debugging_print(instance.get_fields_as_list)
                    job_template_obj.notes.add(instance)
                case "DocumentTemplate":
                    instance = DocumentTemplate.objects.create(
                        **validated_data
                    )  # saving note template object
                    job_template_obj.documents.add(instance)
                case "TaskTemplate":
                    instance = TaskTemplate.objects.create(
                        **validated_data
                    )  # saving note template object
                    job_template_obj.tasks.add(instance)
            # debugging_print(dir(instance._meta))
            # debugging_print(instance._meta.related_objects[0].related_name)
            job_template_obj.save()
            return instance

    class Meta:
        abstract = True
