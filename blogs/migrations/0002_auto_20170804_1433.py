# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]