from django import forms
from core.constants.form import EXCLUDED_FIELDS
from crispy_forms.helper import FormHelper


class BaseModelFormMixin(forms.ModelForm):
    def __init__(self, bookkeeper=None, *args, **kwargs):
        super(BaseModelFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_horizontal = True

    class Meta:
        # pass
        exclude = EXCLUDED_FIELDS
