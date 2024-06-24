# Generated by Django 5.0.6 on 2024-06-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('dob', models.DateField(null=True)),
                ('job_title', models.CharField(max_length=255, null=True)),
                ('joining_date', models.DateField(null=True)),
                ('team', models.CharField(max_length=255, null=True)),
                ('reporting_manager', models.CharField(max_length=255, null=True)),
                ('assigned_assets', models.TextField(null=True)),
                ('allocated_tools', models.TextField(null=True)),
                ('timeline', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
