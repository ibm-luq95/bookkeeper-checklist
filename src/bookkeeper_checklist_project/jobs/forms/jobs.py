from core.forms import BaseModelFormMixin
from jobs.models import Job
from task.models import Task
from django import forms


class JobForm(forms.ModelForm):
    def __init__(self, bookkeeper=None, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        if bookkeeper is not None:
            self.fields["bookkeeper"].initial = bookkeeper
            # self.fields["bookkeeper"].widget.attrs.update({"disabled": "disabled"})
            self.fields["bookkeeper"].widget.attrs.update({"class": "readonly-select"})

    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Job
        exclude = [
            "metadata",
            "is_deleted",
        ]
        # BaseModelFormMixin.Meta.exclude.extend(["tasks", "client"])
