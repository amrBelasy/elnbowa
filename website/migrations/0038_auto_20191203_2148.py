# Generated by Django 2.0.12 on 2019-12-03 21:48

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_auto_20191203_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
