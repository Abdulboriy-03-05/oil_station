# Generated by Django 5.0.4 on 2024-07-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0039_main_xr_income_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elector_xr',
            name='bill',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Elektro svet xisob'),
        ),
    ]