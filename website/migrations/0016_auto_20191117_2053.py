# Generated by Django 2.0.12 on 2019-11-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20191117_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeimage',
            name='cover',
            field=models.ImageField(upload_to=''),
        ),
    ]
