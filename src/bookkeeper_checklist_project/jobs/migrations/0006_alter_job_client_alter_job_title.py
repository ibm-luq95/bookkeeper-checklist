# Generated by Django 4.1.2 on 2022-10-16 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0003_importantcontact_remove_client_business_profile_and_more"),
        ("jobs", "0005_alter_job_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="client",
            field=models.ForeignKey(
                help_text="Client this job belong to",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="client.client",
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="title",
            field=models.CharField(
                help_text="Job Title", max_length=70, verbose_name="title"
            ),
        ),
    ]
