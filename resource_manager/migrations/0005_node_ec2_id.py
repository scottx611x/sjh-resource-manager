# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_manager', '0004_auto_20170306_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='ec2_id',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
