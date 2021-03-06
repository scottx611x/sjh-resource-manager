# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JupyterNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_ip', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('ec2_id', models.CharField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JupyterUser',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('volume_name', models.CharField(blank=True, max_length=500, null=True)),
                ('ebs_volume_id', models.CharField(blank=True, max_length=100, unique=True)),
                ('port', models.CharField(blank=True, choices=[('50001', '50001'), ('50002', '50002'), ('50003', '50003'), ('50004', '50004')], max_length=5, null=True)),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resource_manager.JupyterNode')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='jupyternode',
            unique_together=set([('private_ip', 'ec2_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='jupyteruser',
            unique_together=set([('node', 'port')]),
        ),
    ]
