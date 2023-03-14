# -*- coding: utf-8 -*-#
from django import forms

from core.forms import BaseModelFormMixin
from task.models import TaskTemplate


class TaskTemplateForm(BaseModelFormMixin):
    field_order = ["title", "task_type", "status", "notes"]

    def __int__(self, *args, **kwargs):
        super(TaskTemplateForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = TaskTemplate
