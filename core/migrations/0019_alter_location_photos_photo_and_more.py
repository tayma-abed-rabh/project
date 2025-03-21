# Generated by Django 5.1.4 on 2024-12-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_location_videos_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_photos',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='location_videos',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
