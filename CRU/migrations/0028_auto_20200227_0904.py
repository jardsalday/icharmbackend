# Generated by Django 2.2.5 on 2020-02-27 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRU', '0027_measurement_bmi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='risk_proba',
            new_name='risk_proba1',
        ),
        migrations.AddField(
            model_name='measurement',
            name='risk_proba0',
            field=models.CharField(max_length=100, null=True),
        ),
    ]