from betterforms.multiform import MultiModelForm
from django import forms
from django.db import transaction

from bookkeeper.models import Bookkeeper
from client.models import Client
from core.forms import BaseModelFormMixin, SaveCreatedByFormMixin
from core.utils import debugging_print
from important_contact.forms import ImportantContactForm


class ClientForm(BaseModelFormMixin, SaveCreatedByFormMixin):
    def __init__(self, created_by=None, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields.pop("is_active")

        if created_by is not None:
            self.created_by = created_by

    class Meta(BaseModelFormMixin.Meta):
        model = Client
        # fields = "__all__"
        widgets = {
            "bookkeepers": forms.CheckboxSelectMultiple(),
            "important_contacts": forms.CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        # Save the provided password in hashed format
        client = super().save(commit=False)
        with transaction.atomic():
            if commit:
                client.save()
            important_contacts = self.cleaned_data.get("important_contacts")
            bookkeepers = self.cleaned_data.get("bookkeepers")
            if important_contacts:
                for contact in important_contacts:
                    client.important_contacts.add(contact)
            if bookkeepers:
                for bookkeeper in bookkeepers:
                    client.bookkeepers.add(bookkeeper)
            client.save()
            return client


class ClientCreationMultiForm(MultiModelForm):
    form_classes = {
        "client": ClientForm,
        "important_contact": ImportantContactForm,
    }
