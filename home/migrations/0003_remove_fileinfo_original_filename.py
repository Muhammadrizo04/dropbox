# Generated by Django 5.0.1 on 2024-01-09 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_fileinfo_original_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileinfo',
            name='original_filename',
        ),
    ]
