# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_manager', '0003_auto_20170306_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='users',
            field=models.ManyToManyField(blank=True, to='resource_manager.models.JupyterUser'),
        ),
    ]
