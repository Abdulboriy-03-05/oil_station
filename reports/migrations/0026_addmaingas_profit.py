# Generated by Django 5.0.4 on 2024-07-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0025_alter_add_bank_money_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmaingas',
            name='profit',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Foyda'),
        ),
    ]
