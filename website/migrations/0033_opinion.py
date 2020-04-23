# Generated by Django 2.0.12 on 2019-11-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_auto_20191120_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('job', models.TextField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'الاراء',
            },
        ),
    ]
