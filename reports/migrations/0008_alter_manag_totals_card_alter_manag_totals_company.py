# Generated by Django 5.0.4 on 2024-06-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_alter_manag_add_card_lose_gas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manag_totals',
            name='card',
            field=models.PositiveIntegerField(verbose_name='Plastik karta'),
        ),
        migrations.AlterField(
            model_name='manag_totals',
            name='company',
            field=models.PositiveIntegerField(verbose_name='Tashkilotlar'),
        ),
    ]
