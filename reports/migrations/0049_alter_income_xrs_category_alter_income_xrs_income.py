# Generated by Django 5.0.4 on 2024-07-26 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0048_alter_credit_income_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income_xrs',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='filial', to='reports.filial', verbose_name='Qaysi fililalga'),
        ),
        migrations.AlterField(
            model_name='income_xrs',
            name='income',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='income', to='reports.incomes', verbose_name='Qayerga'),
        ),
    ]