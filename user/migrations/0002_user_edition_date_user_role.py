# Generated by Django 4.0.2 on 2022-02-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='edition_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Sales', 'Sales'), ('Support', 'Support')], max_length=7, null=True),
        ),
    ]
