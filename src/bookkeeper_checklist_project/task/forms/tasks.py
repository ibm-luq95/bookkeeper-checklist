from django import forms
from django_summernote.fields import SummernoteTextFormField

# from django_summernote.fields import SummernoteTextFormField
from core.forms import (
    BaseModelFormMixin,
    SaveCreatedByFormMixin,
    SetSummernoteDynamicAttrsMixin,
)
from jobs.models import Job
from task.models import Task


class TaskForm(BaseModelFormMixin, SaveCreatedByFormMixin, SetSummernoteDynamicAttrsMixin):
    field_order = [
        "title",
        "job",
        "task_type",
        "status",
        "start_date",
        "due_date",
        "additional_notes",
        "hints",
    ]
    additional_notes = SummernoteTextFormField(required=False)

    def __init__(
        self,
        client=None,
        is_disable_job=False,
        job=None,
        created_by=None,
        remove_type_and_status=False,
        remove_job=False,
        set_full_width=False,
        reset_text_widget=False,
        *args,
        **kwargs,
    ):
        super(TaskForm, self).__init__(*args, **kwargs)
        SetSummernoteDynamicAttrsMixin.__init__(
            self, set_full_width=set_full_width, reset_text_widget=reset_text_widget
        )
        self.fields["job"].widget.attrs.update({"class": "input"})

        # check if job passed and set it to job input
        if job is not None:
            self.fields["job"].initial = job

        # this used when update task in bookkeeper dashboard
        if is_disable_job is True:
            self.fields.pop("job")

        # this used in manager client details view, to pass only jobs for custom client
        if self.initial.get("client", None) is not None:
            self.fields["job"].queryset = Job.objects.filter(
                client=self.initial.get("client")
            )
            # self.fields["client"].widget.attrs.update({"class": "cursor-not-allowed readonly-select"})

        if created_by is not None:
            self.created_by = created_by

        if remove_type_and_status is True:
            # self.fields.pop("status")
            self.fields.pop("task_type")
            self.fields.pop("hints")

        if remove_job is True:
            self.fields.pop("job")

    class Meta(BaseModelFormMixin.Meta):
        model = Task
        # widgets = {
        #     "additional_notes": forms.TextInput()
        # }
