# Generated by Django 5.0.4 on 2024-06-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_alter_main_xr_category_main_xr_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aksiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aksiz', models.IntegerField(blank=True, default=680, null=True, verbose_name="Aksiz so'lig'")),
                ('date', models.DateField(auto_now_add=True, verbose_name='Vaqt')),
            ],
            options={
                'verbose_name': " Aksiz so'lig'",
                'verbose_name_plural': " Aksiz so'lig'",
                'ordering': ['-id'],
            },
        ),
    ]
