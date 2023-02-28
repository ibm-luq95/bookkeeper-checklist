from django import forms

from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin
from jobs.models import Job
from task.models import Task


class TaskForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    field_order = [
        "title",
        "job",
        "task_type",
        "task_status",
        "start_date",
        "due_date",
        "additional_notes",
        "hints"
    ]

    def __init__(
        self, client=None, is_disable_job=False, job=None, created_by=None, *args, **kwargs
    ):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields.pop("is_completed")
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

    class Meta(BaseModelFormMixin.Meta):
        model = Task
        widgets = {
            "additional_notes": forms.TextInput()
        }
