# Generated by Django 5.0.4 on 2024-07-02 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0023_addmaingas_elec_sum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_bank_money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.PositiveIntegerField(verbose_name='Sum*')),
                ('date', models.DateField(verbose_name='Vaqt*')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='add_bank_money', to='reports.filial', verbose_name='Add_bank_money')),
            ],
            options={
                'verbose_name': 'Bank ga pul kiritish',
                'verbose_name_plural': 'Bank ga pul kiritish',
            },
        ),
    ]