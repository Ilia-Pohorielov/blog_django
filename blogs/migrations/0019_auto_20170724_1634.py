# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0018_auto_20170724_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('expectation', 'Expectation'), ('no publish', 'No Publish')], default='expectation', max_length=20),
        ),
    ]