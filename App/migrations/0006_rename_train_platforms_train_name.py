# Generated by Django 5.1 on 2024-10-25 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_station_namee_platforms_station_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platforms',
            old_name='train',
            new_name='train_name',
        ),
    ]
