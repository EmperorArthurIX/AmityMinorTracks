# Generated by Django 4.0.6 on 2022-07-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_minortrack_vid_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minortrack',
            name='read_more',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
