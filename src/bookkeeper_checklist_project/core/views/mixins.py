# -*- coding: utf-8 -*-#


class BaseListViewMixin:
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # debugging_print(dir(self.form_class))
        # debugging_print(self.form_class._meta.model._meta)
        if hasattr(self.model, "_meta"):
            context.setdefault("app_label", self.model._meta.app_label)
        return context
