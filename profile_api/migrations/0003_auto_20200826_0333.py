# Generated by Django 3.0.8 on 2020-08-26 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0002_auto_20200826_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_no',
            field=models.CharField(default='', max_length=20),
        ),
    ]
