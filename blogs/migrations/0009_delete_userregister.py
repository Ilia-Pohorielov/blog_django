# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20170720_1650'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegister',
        ),
    ]
