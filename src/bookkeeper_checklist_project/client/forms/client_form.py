from betterforms.multiform import MultiModelForm

from client.models import Client
from core.forms import BaseModelFormMixin
from important_contact.forms import ImportantContactForm


class ClientForm(BaseModelFormMixin):
    def __init__(self, created_by=None, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields.pop("is_active")

        if created_by is not None:
            self.created_by = created_by

    class Meta(BaseModelFormMixin.Meta):
        model = Client
        # fields = "__all__"

    def save(self, commit=True):
        client = super().save(commit=False)
        if self.created_by:
            client.created_by = self.created_by
        if commit:
            client.save()
        return client


class ClientCreationMultiForm(MultiModelForm):
    form_classes = {
        "client": ClientForm,
        "important_contact": ImportantContactForm,
    }
