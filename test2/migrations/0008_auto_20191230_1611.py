# Generated by Django 2.2.5 on 2019-12-30 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0007_auto_20191230_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medicprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
