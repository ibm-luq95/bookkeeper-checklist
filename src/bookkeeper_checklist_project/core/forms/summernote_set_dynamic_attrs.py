# -*- coding: utf-8 -*-#

from django_summernote.fields import SummernoteTextFormField

from core.utils import debugging_print


class SetSummernoteDynamicAttrsMixin:
    def __init__(self, set_full_width=False):
        if set_full_width is True:
            for field_name in self.fields:
                debugging_print(field_name)
                if isinstance(self.fields.get(field_name), SummernoteTextFormField):
                    self.fields[field_name].widget.attrs.update(
                        {"summernote": {"width": "100%"}}
                    )