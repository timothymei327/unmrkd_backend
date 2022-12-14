# Generated by Django 4.1.1 on 2022-09-12 23:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unmrkd', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='photo_url',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='hashtags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=10),
        ),
    ]
