from core.forms import BaseModelFormMixin
from important_contact.models import ImportantContact


class ImportantContactForm(BaseModelFormMixin):
    # auto_id = "important_contact_%s"

    def __init__(self, is_readonly=False, is_creating=False, *args, **kwargs):
        super(ImportantContactForm, self).__init__(*args, **kwargs)
        # print(is_creating)
        self.fields["contact_website"].widget.attrs.update(
            {"class": "input", "type": "url"}
        )
        if is_readonly is True:
            for field in self.fields:
                self.fields[field].widget.attrs.update({"readonly": "readonly"})

    class Meta(BaseModelFormMixin.Meta):
        model = ImportantContact
        # exclude = ["client", "metadata", "is_deleted"]
        # widgets = {
        #     "account_url": forms.URLInput()
        # }
