# Generated by Django 2.0.12 on 2019-12-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_auto_20191203_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='video',
            field=models.TextField(),
        ),
    ]
