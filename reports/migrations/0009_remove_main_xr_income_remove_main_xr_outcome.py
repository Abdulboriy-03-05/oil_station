# Generated by Django 5.0.4 on 2024-06-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_rename_main_xr_main_xr_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_xr',
            name='income',
        ),
        migrations.RemoveField(
            model_name='main_xr',
            name='outcome',
        ),
    ]
