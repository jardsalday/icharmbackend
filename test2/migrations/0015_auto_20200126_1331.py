# Generated by Django 2.2.5 on 2020-01-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0014_medicuserprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicuserprofile',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientuserprofile',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
