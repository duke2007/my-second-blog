# Generated by Django 2.0.7 on 2018-07-16 05:27

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0003_auto_20180714_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='Text'),
        ),
    ]
