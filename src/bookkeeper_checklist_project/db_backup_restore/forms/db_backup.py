# -*- coding: utf-8 -*-#
from django import forms
import pyminizip
from django.conf import settings
from django.core import management
from django.core.management.commands import dumpdata
from django.core.files.base import ContentFile, File
from django.db import transaction

from core.forms import BaseModelFormMixin
from core.utils import debugging_print
from db_backup_restore.models import DBBackup

EXCLUDED = (
    "auth.Permission",
    "contenttypes.ContentType",
    "sessions.Session",
)


class BackupForm(BaseModelFormMixin):
    field_order = ["name", "apps", "status"]

    def __init__(self, *args, **kwargs):
        super(BackupForm, self).__init__(*args, **kwargs)
        # self.fields["apps"].queryset = ContentType.objects.filter(
        #     ~Q(app_label__in=excluded_apps), ~Q(model__in=excluded_models)
        # )
        # debugging_print(ContentType.objects.filter().first().name)

    class Meta(BaseModelFormMixin.Meta):
        model = DBBackup

    def save(self, commit=True):
        backup_obj = super().save(commit=False)
        name = self.cleaned_data.get("name")
        backup_file = settings.BASE_DIR / "db_backups" / f"{name}.json"
        try:
            # Save the provided password in hashed format
            with transaction.atomic():
                # debugging_print(dir(backup_obj.backup_path))
                if backup_file.exists() is True:
                    raise forms.ValidationError(f"Backup file exists - {backup_file}")
                with open(backup_file, "w") as f:
                    management.call_command(
                        dumpdata.Command(),
                        exclude=EXCLUDED,
                        # natural_foreign=True,
                        # natural_primary=True,
                        format="json",
                        indent=4,
                        stdout=f,
                    )
                # backup_obj.backup_path.name = f"{name}.json"
                password = "123"
                # compress level
                com_lvl = 5
                # output file
                output_path = settings.BASE_DIR / "db_backups" / f"{name}.zip"
                pyminizip.compress(backup_file.as_posix(), None, output_path.as_posix(), password, com_lvl)
                backup_obj.backup_path.name = f"{name}.zip"

                if commit:
                    backup_obj.save()

                backup_file.unlink()

                return backup_obj
        except Exception as ex:
            if backup_file.exists() is True:
                backup_file.unlink()
            raise forms.ValidationError(str(ex), code="invalid")
