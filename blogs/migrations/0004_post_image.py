# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='logo.png', upload_to='post_images'),
            preserve_default=False,
        ),
    ]
