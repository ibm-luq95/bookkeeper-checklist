# Generated by Django 4.1.2 on 2022-10-23 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assistant", "0005_assistant_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="assistant",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="is_deleted"),
        ),
    ]