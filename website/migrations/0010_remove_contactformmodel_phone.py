# Generated by Django 2.2.4 on 2019-10-28 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20191028_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactformmodel',
            name='phone',
        ),
    ]
