# Generated by Django 2.0.12 on 2019-11-18 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20191118_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depart1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
