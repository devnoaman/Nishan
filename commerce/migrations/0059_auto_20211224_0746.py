# Generated by Django 3.2.9 on 2021-12-24 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0058_auto_20211217_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centeropinion',
            name='user',
        ),
        migrations.RemoveField(
            model_name='serviceopinion',
            name='user',
        ),
    ]