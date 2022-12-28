from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext as _

from bookkeeper.models import Bookkeeper
from core.forms import BaseModelFormMixin
from jobs.models import Job


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
        queryset=Bookkeeper.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def clean_due_date(self):
        data = self.cleaned_data["due_date"]
        now = timezone.now().date()

        if data < now:
            raise ValidationError(_("Due date not valid!"), code="invalid")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    class Meta(BaseModelFormMixin.Meta):
        model = Job
        widgets = {
            "due_date": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "note": forms.TextInput(),
        }
