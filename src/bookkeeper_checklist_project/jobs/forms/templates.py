# -*- coding: utf-8 -*-#
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin
from jobs.models import JobTemplate


class JobTemplateForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    def __init__(
        self,
        created_by=None,
        is_updated=False,
        *args,
        **kwargs,
    ):
        super(JobTemplateForm, self).__init__(*args, **kwargs)
        if created_by is not None:
            self.created_by = created_by

    def save(self, commit=True):
        job_template_obj = super().save(commit=False)
        if commit:
            job_template_obj.save()
            self.save_m2m()
        return job_template_obj

    class Meta(BaseModelFormMixin.Meta):
        model = JobTemplate
