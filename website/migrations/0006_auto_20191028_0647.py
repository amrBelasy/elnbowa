# Generated by Django 2.2.4 on 2019-10-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20191027_0330'),
    ]

    # operations = [
    #     migrations.CreateModel(
    #         name='Agenda',
    #         fields=[
    #             ('id', models.BigAutoField(primary_key=True, serialize=False)),
    #             ('name', models.CharField(max_length=150)),
    #             ('description', models.TextField(max_length=500)),
    #             ('agenda_type', models.CharField(max_length=50)),
    #             ('start_date', models.DateField()),
    #             ('end_date', models.DateField()),
    #             ('time', models.TimeField(blank=True, null=True)),
    #             ('dateCreated', models.DateTimeField(auto_now_add=True)),
    #             ('dateUpdated', models.DateTimeField(auto_now=True)),
    #         ],
    #     ),
    #     migrations.CreateModel(
    #         name='Image',
    #         fields=[
    #             ('id', models.BigAutoField(primary_key=True, serialize=False)),
    #             ('name', models.CharField(blank=True, max_length=150, null=True)),
    #         ],
    #     ),
    #     migrations.RemoveField(
    #         model_name='contactformmodel',
    #         name='phone',
    #     ),
    #     migrations.CreateModel(
    #         name='Gallery',
    #         fields=[
    #             ('id', models.BigAutoField(primary_key=True, serialize=False)),
    #             ('name', models.CharField(blank=True, max_length=150, null=True)),
    #             ('description', models.TextField(blank=True, max_length=500, null=True)),
    #             ('dateCreated', models.DateTimeField(auto_now_add=True)),
    #             ('dateUpdated', models.DateTimeField(auto_now=True)),
    #             ('image', models.ManyToManyField(to='website.Image')),
    #         ],
    #     ),
    # ]
