# Generated by Django 4.2.11 on 2024-09-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_apiinfo_sample_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='sample_data',
            field=models.JSONField(),
        ),
    ]
