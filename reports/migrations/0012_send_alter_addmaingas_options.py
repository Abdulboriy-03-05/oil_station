# Generated by Django 5.0.4 on 2024-06-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_others'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_tax', models.IntegerField(blank=True, default=0, null=True, verbose_name="Pul o'tkazish %'")),
                ('date', models.DateField(auto_now_add=True, verbose_name='Vaqt')),
            ],
            options={
                'verbose_name': "Pul o'tkazish %",
                'verbose_name_plural': "Pul o'tkazish %",
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='addmaingas',
            options={'ordering': ['-id'], 'verbose_name': 'Asosiy gaz xisoblagich', 'verbose_name_plural': 'Asosiy gaz xisoblagich'},
        ),
    ]