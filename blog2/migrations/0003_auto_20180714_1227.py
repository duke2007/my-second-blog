# Generated by Django 2.0.7 on 2018-07-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
