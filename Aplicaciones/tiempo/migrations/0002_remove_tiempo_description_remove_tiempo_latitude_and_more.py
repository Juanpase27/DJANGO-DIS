# Generated by Django 4.2.6 on 2023-11-17 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiempo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiempo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tiempo',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='tiempo',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='tiempo',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='tiempo',
            name='url',
        ),
        migrations.RemoveField(
            model_name='tiempo',
            name='wind_speed',
        ),
    ]
