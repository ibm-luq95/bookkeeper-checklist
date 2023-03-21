# -*- coding: utf-8 -*-#
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class SlugifyMixin(models.Model):
    slug = models.SlugField(
        _("slug"), max_length=250, null=True, blank=True, unique=True, db_index=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if hasattr(self, "title"):
            self.slug = slugify(self.title)
        elif hasattr(self, "name"):
            self.slug = slugify(self.name)
        super(SlugifyMixin, self).save(*args, **kwargs)
