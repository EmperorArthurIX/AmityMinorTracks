# Generated by Django 4.0.6 on 2022-07-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='minortrack',
            name='vid_thumbnail',
            field=models.ImageField(default='', upload_to='thumbnails'),
            preserve_default=False,
        ),
    ]
