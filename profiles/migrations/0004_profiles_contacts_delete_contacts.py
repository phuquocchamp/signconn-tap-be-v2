# Generated by Django 5.0 on 2023-12-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_contacts_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='contacts',
            field=models.JSONField(default=list),
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]
