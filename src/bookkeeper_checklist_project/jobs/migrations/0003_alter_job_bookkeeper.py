# Generated by Django 4.1.1 on 2022-10-04 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookkeeper", "0004_alter_bookkeeper_options"),
        ("jobs", "0002_job_bookkeeper"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="bookkeeper",
            field=models.ForeignKey(
                help_text="Bookkeeper of the job",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="jobs",
                to="bookkeeper.bookkeeper",
            ),
        ),
    ]
