# -*- coding: utf-8 -*-#
from django import forms

from site_settings.models import SiteSettings
from core.forms import BaseModelFormMixin


class SiteSettingsForm(BaseModelFormMixin):
    def __init__(self, *args, **kwargs):
        super(SiteSettingsForm, self).__init__(*args, **kwargs)
        self.fields["url"].widget.attrs.update({"class": "input", "type": "url"})
        self.fields["facebook"].widget.attrs.update({"class": "input", "type": "url"})
        self.fields["youtube"].widget.attrs.update({"class": "input", "type": "url"})
        self.fields["instagram"].widget.attrs.update({"class": "input", "type": "url"})
        self.fields["twitter"].widget.attrs.update({"class": "input", "type": "url"})
        self.fields["slug"].widget.attrs.update({"readonly": "readonly"})

    class Meta(BaseModelFormMixin.Meta):
        model = SiteSettings
        exclude = ["metadata", "is_deleted", "deleted_at"]
