# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_manager', '0008_auto_20170306_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='port',
            field=models.CharField(choices=[('PORT_50001', '50001'), ('PORT_50002', '50002'), ('PORT_50003', '50003'), ('PORT_50004', '50004')], default='PORT_50001', max_length=5),
        ),
        migrations.AlterField(
            model_name='node',
            name='ec2_id',
            field=models.CharField(max_length=100),
        ),
    ]
