# Generated by Django 5.1 on 2024-10-25 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_platforms_train_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platforms',
            old_name='station_name',
            new_name='station_names',
        ),
        migrations.RenameField(
            model_name='platforms',
            old_name='train_name',
            new_name='train_names',
        ),
    ]
