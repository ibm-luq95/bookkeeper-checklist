from django import forms

from bookkeeper.models import Bookkeeper
from core.forms import BaseModelFormMixin
from jobs.models import Job
from task.models import Task


class JobForm(BaseModelFormMixin):
    def __init__(self, bookkeeper=None, client=None, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        if bookkeeper is not None:
            self.fields["bookkeeper"].initial = bookkeeper
            # self.fields["bookkeeper"].widget.attrs.update({"disabled": "disabled"})
            self.fields["bookkeeper"].widget.attrs.update({"class": "readonly-select"})
        if client is not None:
            self.fields["client"].initial = client
            self.fields["client"].widget.attrs.update({"class": "readonly-select"})

    bookkeeper = forms.ModelMultipleChoiceField(
        queryset=Bookkeeper.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta(BaseModelFormMixin.Meta):
        model = Job
        widgets = {
            "due_date": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "note": forms.TextInput(),
        }
