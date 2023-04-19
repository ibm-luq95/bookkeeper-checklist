# -*- coding: utf-8 -*-#

# from django_summernote.fields import SummernoteTextFormField

from core.utils import debugging_print
from django import forms


class SetSummernoteDynamicAttrsMixin:
    def __init__(self):
        pass
        # for field_name in self.fields:
            # debugging_print(field_name)
            # debugging_print(self.fields.get(field_name).widget)
            # print("############")
            # if isinstance(self.fields.get(field_name).widget, forms.Textarea):
                # debugging_print(field_name)
                # widget = self.fields.get(field_name).widget
                # widget.attrs.update({"class": "rich-textarea"})
                # debugging_print(widget.attrs.get("class"))

            #     self.fields[field_name].widget.attrs.update(
            #         {"summernote": {"width": "100%"}}
            #     )
