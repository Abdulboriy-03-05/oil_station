# Generated by Django 5.0.4 on 2024-06-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0014_aksiz_xr'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmaingas',
            name='aksiz',
            field=models.IntegerField(blank=True, null=True, verbose_name='Aksiz narx'),
        ),
        migrations.AddField(
            model_name='addmaingas',
            name='aksiz_sum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Aksiz narxi'),
        ),
    ]