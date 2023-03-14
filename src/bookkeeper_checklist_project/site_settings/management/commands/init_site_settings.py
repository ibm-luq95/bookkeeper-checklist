# -*- coding: utf-8 -*-#

from django.core.management.base import BaseCommand
from django.db import transaction

from core.management.mixins import CommandStdOutputMixin
from site_settings.models import SiteSettings


class Command(BaseCommand, CommandStdOutputMixin):
    help = "Initialize web application settings"

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                data = {
                    "slug": "web app",
                    "email": "bookkeeper_checklist_app@email.com",
                    "name": "Bookkeeper Checklist App",
                }
                site_settings = SiteSettings.objects.select_related().create(**data)
                print(site_settings)
                self.stdout_output("success", "Site Settings Created Successfully!")
        except Exception as ex:
            self.stdout_output("error", str(ex))
