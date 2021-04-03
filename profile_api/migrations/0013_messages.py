# Generated by Django 3.0.8 on 2020-09-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0012_auto_20200901_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=255)),
                ('messages', models.CharField(max_length=1024)),
            ],
        ),
    ]
