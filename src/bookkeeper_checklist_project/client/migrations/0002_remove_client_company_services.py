# Generated by Django 4.1.3 on 2022-11-21 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="company_services",
        ),
    ]
