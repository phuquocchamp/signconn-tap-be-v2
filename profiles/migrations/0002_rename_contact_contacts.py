# Generated by Django 5.0 on 2023-12-30 12:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Contact",
            new_name="Contacts",
        ),
    ]
