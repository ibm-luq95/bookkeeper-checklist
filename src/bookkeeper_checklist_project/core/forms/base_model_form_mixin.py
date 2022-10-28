from django import forms
from crispy_forms.helper import FormHelper


class BaseModelFormMixin(forms.ModelForm):
    def __init__(self, bookkeeper=None, *args, **kwargs):
        super(BaseModelFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        # pass
        exclude = [
            "metadata",
            "is_deleted",
        ]
