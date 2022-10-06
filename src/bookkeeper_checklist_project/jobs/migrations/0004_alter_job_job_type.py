# Generated by Django 4.1.1 on 2022-10-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_alter_job_bookkeeper"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="job_type",
            field=models.CharField(
                choices=[
                    ("no_type", "No Type"),
                    ("recurring", "Recurring"),
                    ("weekly", "Weekly"),
                    ("monthly", "Monthly"),
                    ("quarterly", "Quarterly"),
                    ("yearly", "Yearly"),
                    ("one_time", "One Time"),
                    ("urgent", "Urgent"),
                ],
                help_text="Type of this job, Recurring, Weekly, Urgent,..etc",
                max_length=20,
                verbose_name="job_type",
            ),
        ),
    ]
