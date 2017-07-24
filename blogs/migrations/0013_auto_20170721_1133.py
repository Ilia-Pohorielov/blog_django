# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('publish', 'Publish'), ('expectation', 'Expectation'), ('no publish', 'No Publish')], default='expectation', max_length=20),
            preserve_default=False,
        ),
    ]