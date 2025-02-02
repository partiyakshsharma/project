# Generated by Django 5.0.2 on 2024-04-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('company_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('website', models.URLField()),
                ('job_location', models.CharField(max_length=100)),
                ('employees', models.CharField(max_length=100)),
                ('locations', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('founded', models.CharField(max_length=100)),
                ('revenue', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('all_location_info', models.TextField()),
            ],
        ),
    ]
