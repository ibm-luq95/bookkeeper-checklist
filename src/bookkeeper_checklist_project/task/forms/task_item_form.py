# -*- coding: utf-8 -*-#
from core.forms import BaseModelFormMixin
from task.models import TaskItem


class TaskItemForm(BaseModelFormMixin):
    field_order = ["title"]

    def __int__(self, *args, **kwargs):
        super(TaskItemForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = TaskItem
