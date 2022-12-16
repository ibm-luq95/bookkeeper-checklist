# -*- coding: utf-8 -*-#

from django.core.management.base import BaseCommand
from django.db import transaction

from site_settings.models import SiteSettings


class Command(BaseCommand):
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

    def stdout_output(self, type, msg):
        if type == "error":
            self.stdout.write(self.style.ERROR(msg))
        elif type == "success":
            self.stdout.write(self.style.SUCCESS(msg))
        elif type == "info":
            self.stdout.write(self.style.NOTICE(msg))
        elif type == "warn":
            self.stdout.write(self.style.WARNING(msg))
