# Generated by Django 4.0.2 on 2022-02-11 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='comments',
        ),
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
