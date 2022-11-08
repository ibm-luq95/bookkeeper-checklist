from core.forms import BaseModelFormMixin
from task.models import Task
from django import forms


class TaskForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

    class Meta(BaseModelFormMixin.Meta):
        model = Task
        widgets = {
            "start_date": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "due_date": forms.DateInput(attrs={"class": "input", "type": "date"}),
        }
