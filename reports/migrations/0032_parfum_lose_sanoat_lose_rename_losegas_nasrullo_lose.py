# Generated by Django 5.0.4 on 2024-07-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0031_addmaingas_lose_gas_addmaingas_remain_gas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parfum_lose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('losegas', models.FloatField(blank=True, default=1.4, null=True, verbose_name="1.4% Tabiy Yo'qotish")),
                ('date', models.DateField(auto_now_add=True, verbose_name='Vaqt')),
            ],
            options={
                'verbose_name': " Gazni 1.4% Yo'qotish",
                'verbose_name_plural': " Gazni 1.4% Yo'qotish",
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Sanoat_lose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('losegas', models.FloatField(blank=True, default=1.4, null=True, verbose_name="1.4% Tabiy Yo'qotish")),
                ('date', models.DateField(auto_now_add=True, verbose_name='Vaqt')),
            ],
            options={
                'verbose_name': " Gazni 1.4% Yo'qotish",
                'verbose_name_plural': " Gazni 1.4% Yo'qotish",
                'ordering': ['-id'],
            },
        ),
        migrations.RenameModel(
            old_name='Losegas',
            new_name='Nasrullo_lose',
        ),
    ]
