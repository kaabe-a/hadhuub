# Generated by Django 4.0.5 on 2022-06-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20220615_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover',
            field=models.ImageField(default='cover.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(default='avatar.jpg', upload_to=''),
        ),
    ]
