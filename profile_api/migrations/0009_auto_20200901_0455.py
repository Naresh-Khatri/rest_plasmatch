# Generated by Django 3.0.8 on 2020-09-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0008_auto_20200831_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorprofile',
            name='lat',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='donorprofile',
            name='lng',
            field=models.CharField(default='', max_length=10),
        ),
    ]
