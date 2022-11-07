from django import forms

from core.forms import BaseModelFormMixin
from jobs.models import Job
from task.models import Task


class JobForm(BaseModelFormMixin):
    def __init__(self, bookkeeper=None, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        if bookkeeper is not None:
            self.fields["bookkeeper"].initial = bookkeeper
            # self.fields["bookkeeper"].widget.attrs.update({"disabled": "disabled"})
            self.fields["bookkeeper"].widget.attrs.update({"class": "readonly-select"})

    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta(BaseModelFormMixin.Meta):
        model = Job
        widgets = {
            "due_date": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "note": forms.TextInput(),
        }
