# Generated by Django 2.0.12 on 2019-11-18 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_auto_20191118_0353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformmodel',
            options={'verbose_name_plural': 'التواصل معنا'},
        ),
        migrations.AlterModelOptions(
            name='depart1',
            options={'verbose_name_plural': 'قسم الاعشاب'},
        ),
        migrations.AlterModelOptions(
            name='depart2',
            options={'verbose_name_plural': 'قسم الرقية الشرعية'},
        ),
        migrations.AlterModelOptions(
            name='homeimage',
            options={'verbose_name_plural': 'الرئيسية'},
        ),
    ]
