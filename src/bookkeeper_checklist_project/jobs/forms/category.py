from core.forms import (
    BaseModelFormMixin,
)
from jobs.models import JobCategory


class JobCategoryForm(BaseModelFormMixin):
    def __int__(self, *args, **kwargs):
        super(JobCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JobCategory
        fields = ["name"]
