# Generated by Django 4.0.4 on 2022-11-17 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transcript',
            old_name='info',
            new_name='tittle',
        ),
    ]