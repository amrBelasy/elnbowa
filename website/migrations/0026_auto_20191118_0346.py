# Generated by Django 2.0.12 on 2019-11-18 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_contactformmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformmodel',
            options={'verbose_name': 'التواصل معنا'},
        ),
        migrations.AlterModelOptions(
            name='depart1',
            options={'verbose_name': 'قسم الاعشاب'},
        ),
        migrations.AlterModelOptions(
            name='depart2',
            options={'verbose_name': 'الرقية الشرعية'},
        ),
        migrations.AlterModelOptions(
            name='homeimage',
            options={'verbose_name': 'الرئيسية'},
        ),
        migrations.AlterModelTable(
            name='depart1',
            table=None,
        ),
        migrations.AlterModelTable(
            name='depart2',
            table=None,
        ),
        migrations.AlterModelTable(
            name='homeimage',
            table=None,
        ),
    ]