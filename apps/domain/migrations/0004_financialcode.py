# Generated by Django 3.1.2 on 2021-03-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_activitysubcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialCode',
            fields=[
                ('financial_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('financial_desc', models.CharField(max_length=255)),
            ],
        ),
    ]
