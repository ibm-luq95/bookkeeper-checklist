# Generated by Django 4.1 on 2022-08-05 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("client", "0001_initial"),
        ("company_services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assistant",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "metadata",
                    models.JSONField(
                        blank=True, default=dict, null=True, verbose_name="metadata"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="updated_at"
                    ),
                ),
                ("slug", models.SlugField(max_length=250, null=True, verbose_name="slug")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("enabled", "Enabled"),
                            ("pending", "Pending"),
                            ("canceled", "Canceled"),
                            ("disabled", "Disabled"),
                        ],
                        default="enabled",
                        max_length=10,
                        verbose_name="status",
                    ),
                ),
                (
                    "assistant_type",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("marketing", "Marketing"),
                            ("admin", "Admin"),
                            ("bookkeeping", "Bookkeeping"),
                        ],
                        default="all",
                        max_length=15,
                        verbose_name="assistant_type",
                    ),
                ),
                ("clients", models.ManyToManyField(to="client.client")),
                (
                    "company_services",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="assistant",
                        to="company_services.companyservice",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "permissions": [
                    ("can_access_bookkeeper", "Can access bookkeeper account details"),
                    ("can_edit_bookkeeper", "Can edit bookkeeper account details"),
                    ("can_access_client", "Can access client(s) account details"),
                ],
                "abstract": False,
            },
        ),
    ]
