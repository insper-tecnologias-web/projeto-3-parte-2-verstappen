# Generated by Django 5.1.2 on 2024-10-22 16:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apiF1", "0004_driver_driverid_team_teamid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="driver",
            name="name",
        ),
        migrations.RemoveField(
            model_name="team",
            name="name",
        ),
    ]
