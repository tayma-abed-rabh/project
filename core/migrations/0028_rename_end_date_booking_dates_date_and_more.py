# Generated by Django 5.1.4 on 2025-02-13 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_sync_lips_generated_video_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_dates',
            old_name='end_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='booking_dates',
            name='start_date',
        ),
    ]
