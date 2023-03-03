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

    class Meta(BaseModelFormMixin.Meta):
        model = JobTemplate
