# Generated by Django 4.0.6 on 2022-08-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_minortrack_vid_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='minortrack',
            name='max_seats',
            field=models.PositiveSmallIntegerField(default=70),
            preserve_default=False,
        ),
    ]