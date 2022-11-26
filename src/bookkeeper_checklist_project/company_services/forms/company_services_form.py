from company_services.models import CompanyService
from core.forms import BaseModelFormMixin


class CompanyServiceForm(BaseModelFormMixin):
    def __init__(self, client=None, *args, **kwargs):
        super(CompanyServiceForm, self).__init__(*args, **kwargs)
        self.fields["url"].widget.attrs.update({"class": "input", "type": "url"})
        if client is not None:
            self.fields["client"].initial = client
        #     # self.fields["bookkeeper"].widget.attrs.update({"disabled": "disabled"})
        #     self.fields["bookkeeper"].widget.attrs.update({"class": "readonly-select"})

    class Meta(BaseModelFormMixin.Meta):
        model = CompanyService
