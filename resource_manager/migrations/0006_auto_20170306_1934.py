# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_manager', '0005_node_ec2_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='ec2_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
