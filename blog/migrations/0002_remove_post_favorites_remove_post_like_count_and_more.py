# Generated by Django 4.0.4 on 2022-05-20 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
