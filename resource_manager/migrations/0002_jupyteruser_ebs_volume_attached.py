# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jupyteruser',
            name='ebs_volume_attached',
            field=models.BooleanField(default=False),
        ),
    ]
