from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext as _

from assistant.models import Assistant
from bookkeeper.models import Bookkeeper
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin
from jobs.models import Job


class JobForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    def __init__(
        self,
        bookkeeper=None,
        client=None,
        created_by=None,
        is_updated=False,
        *args,
        **kwargs
    ):
        super(JobForm, self).__init__(*args, **kwargs)
        if bookkeeper is not None:
            self.fields["bookkeeper"].initial = bookkeeper
            # self.fields["bookkeeper"].widget.attrs.update({"disabled": "disabled"})
            self.fields["bookkeeper"].widget.attrs.update(
                {"class": "readonly-select cursor-not-allowed"}
            )
        if client is not None:
            self.fields["client"].initial = client
            self.fields["client"].widget.attrs.update(
                {"class": "readonly-select cursor-not-allowed"}
            )

        if created_by is not None:
            self.created_by = created_by

        self.is_update = is_updated

    bookkeeper = forms.ModelMultipleChoiceField(
        queryset=Bookkeeper.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    assistants = forms.ModelMultipleChoiceField(
        queryset=Assistant.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    def clean_due_date(self):
        data = self.cleaned_data["due_date"]
        now = timezone.now().date()

        if self.is_update is False:
            if data < now:
                raise ValidationError(_("Due date not valid!"), code="invalid")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    class Meta(BaseModelFormMixin.Meta):
        model = Job
        widgets = {
            "note": forms.TextInput(),
        }
