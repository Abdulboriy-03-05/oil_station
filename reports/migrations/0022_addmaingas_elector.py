# Generated by Django 5.0.4 on 2024-07-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0021_addmaingas_card_addmaingas_chec_addmaingas_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmaingas',
            name='elector',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name="Elektor solig' narxi"),
        ),
    ]
