# Generated by Django 3.1.2 on 2021-03-12 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('source_url', models.URLField(blank=True, unique=True)),
                ('source_html', models.TextField(blank=True, null=True)),
                ('source_text', models.TextField(blank=True, null=True)),
                ('source_date', models.DateTimeField(blank=True, null=True)),
                ('date_added', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('current_status', models.CharField(blank=True, choices=[('SRCM', 'sourced_m'), ('EXTM', 'extracted_m')], default='SRCM', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SourceCode',
            fields=[
                ('source_code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('source_desc', models.CharField(max_length=255)),
            ],
        ),
    ]