# Generated by Django 3.0.8 on 2020-08-26 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0003_auto_20200826_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=255)),
                ('blood_type', models.CharField(max_length=3)),
                ('case_sheet_form', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DonorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes', models.BooleanField(default=False)),
                ('lungs', models.BooleanField(default=False)),
                ('kidney', models.BooleanField(default=False)),
                ('high_bp', models.BooleanField(default=False)),
                ('liver', models.BooleanField(default=False)),
                ('have_aadhar', models.BooleanField(default=True)),
                ('blood_type', models.CharField(max_length=3)),
                ('drinks_14', models.BooleanField(default=False)),
                ('discharge_report', models.BooleanField(default=True)),
                ('neg_2weeks', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
