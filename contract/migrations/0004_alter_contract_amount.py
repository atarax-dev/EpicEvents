# Generated by Django 4.0.2 on 2022-02-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_alter_contract_signature_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
