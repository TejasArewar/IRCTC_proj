# Generated by Django 5.1 on 2024-10-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_alter_platforms_train_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='trains',
            name='running_days',
            field=models.CharField(default='W-T-F'),
        ),
    ]
