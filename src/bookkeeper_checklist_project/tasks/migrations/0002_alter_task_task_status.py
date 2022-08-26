# Generated by Django 4.1 on 2022-08-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="task_status",
            field=models.CharField(
                choices=[
                    ("not_started", "Not Started"),
                    ("in_progress", "In progress"),
                    ("past_due", "Past Due"),
                    ("complete", "Complete"),
                    ("archive", "Archive"),
                ],
                default="not_started",
                max_length=20,
                verbose_name="task_status",
            ),
        ),
    ]