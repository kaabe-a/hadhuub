# Generated by Django 4.0.5 on 2022-07-18 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_social_github'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='profile',
        ),
        migrations.AddField(
            model_name='social',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
