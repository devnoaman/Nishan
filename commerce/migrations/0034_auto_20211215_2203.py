# Generated by Django 3.2.9 on 2021-12-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0033_auto_20211215_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='time'),
        ),
        migrations.AlterField(
            model_name='center',
            name='open_days',
            field=models.DurationField(blank=True, max_length=255, null=True, verbose_name='open_days'),
        ),
    ]