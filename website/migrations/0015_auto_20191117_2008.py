# Generated by Django 2.0.12 on 2019-11-17 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_homeimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_work',
            name='name',
        ),
        migrations.DeleteModel(
            name='Team_Work',
        ),
    ]
