# Generated by Django 4.1 on 2022-08-12 16:33

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Manager",
            fields=[],
            options={
                "permissions": [("can_view_dashboard", "Can View Dashboard")],
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("users.customuser",),
        ),
    ]
