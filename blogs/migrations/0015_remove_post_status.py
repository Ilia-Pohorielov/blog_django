# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_auto_20170721_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
