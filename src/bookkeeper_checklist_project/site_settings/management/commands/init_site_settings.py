# -*- coding: utf-8 -*-#

from django.core.management.base import BaseCommand
from django.db import transaction

from core.management.mixins import CommandStdOutputMixin
from site_settings.models import SiteSettings, ApplicationConfigurations


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
                # site_settings = SiteSettings.objects.select_related().create(**data)
                site_settings, created = SiteSettings.objects.get_or_create(
                    slug="web-app", defaults=data
                )
                app_configs, created2 = ApplicationConfigurations.objects.get_or_create(
                    slug="app-configs"
                )
                self.stdout_output("success", site_settings)
                self.stdout_output("success", app_configs)
                self.stdout_output(
                    "success",
                    "Site Settings & Application Configurations Created Successfully!",
                )
        except Exception as ex:
            self.stdout_output("error", str(ex))
