from crispy_forms.helper import FormHelper
from django import forms

from core.constants.form import EXCLUDED_FIELDS
from .html5_mixin import Html5Mixin


class BaseModelFormMixin(Html5Mixin, forms.ModelForm):
    def __init__(self, bookkeeper=None, *args, **kwargs):
        super(BaseModelFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_horizontal = True

    class Meta:
        exclude = EXCLUDED_FIELDS
