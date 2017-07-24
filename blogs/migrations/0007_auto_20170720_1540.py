# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 12:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0006_auto_20170720_1339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userregister',
            options={},
        ),
        migrations.AlterModelManagers(
            name='userregister',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userregister',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='userregister',
            name='id',
            field=models.AutoField(auto_created=True, default=10, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userregister',
            name='user',
            field=models.OneToOneField(default=10, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userregister',
            name='avatar',
            field=models.ImageField(upload_to='post_images/avatar', verbose_name='Изображение'),
        ),
    ]