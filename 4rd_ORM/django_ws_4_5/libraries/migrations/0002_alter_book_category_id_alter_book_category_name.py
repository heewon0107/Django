# Generated by Django 4.2.9 on 2024-09-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
