# Generated by Django 2.0.12 on 2019-12-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0042_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='video',
            field=models.URLField(),
        ),
    ]