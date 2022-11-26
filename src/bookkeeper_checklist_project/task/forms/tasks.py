from django import forms

from core.forms import BaseModelFormMixin
from task.models import Task


class TaskForm(BaseModelFormMixin):
    def __init__(self, client=None, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields.pop("user")
        if client is not None:
            self.fields["client"].initial = client
            self.fields["client"].widget.attrs.update({"class": "readonly-select"})

    class Meta(BaseModelFormMixin.Meta):
        model = Task
        widgets = {
            "start_date": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "due_date": forms.DateInput(attrs={"class": "input", "type": "date"}),
        }
