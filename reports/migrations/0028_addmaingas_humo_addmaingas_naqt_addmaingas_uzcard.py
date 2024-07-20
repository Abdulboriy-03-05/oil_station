# Generated by Django 5.0.4 on 2024-07-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0027_alter_main_xr_outcome_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmaingas',
            name='humo',
            field=models.BooleanField(default=False, verbose_name='Humo'),
        ),
        migrations.AddField(
            model_name='addmaingas',
            name='naqt',
            field=models.BooleanField(default=False, verbose_name='Naqt'),
        ),
        migrations.AddField(
            model_name='addmaingas',
            name='uzcard',
            field=models.BooleanField(default=False, verbose_name='Uzcard'),
        ),
    ]
