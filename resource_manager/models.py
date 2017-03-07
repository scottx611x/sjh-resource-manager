from __future__ import unicode_literals

import boto3
from django.db import models


class JupyterNode(models.Model):
    MAX_USERS = 4
    private_ip = models.GenericIPAddressField(protocol="IPv4", blank=True,
                                              null=True)
    ec2_id = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        unique_together = (("private_ip", "ec2_id"),)

    def __str__(self):
        return "{}: {}".format(
            self.private_ip, self.ec2_id
        )

    def get_status(self):
        ec2_client = boto3.client('ec2')
        waiter.wait(
            DryRun=True | False,
            InstanceIds=[
                'string',
            ],
            Filters=[
                {
                    'Name': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ],
            NextToken='string',
            MaxResults=123
        )


class JupyterUser(models.Model):
    PORTS = (
        ("50001", '50001'),
        ("50002", '50002'),
        ("50003", '50003'),
        ("50004", '50004')
    )

    email = models.EmailField(unique=True, primary_key=True)
    volume_name = models.CharField(max_length=500, blank=True, null=True)
    ebs_volume_id = models.CharField(max_length=100, blank=True, unique=True)
    node = models.ForeignKey(JupyterNode, blank=True, null=True)
    port = models.CharField(max_length=5, choices=PORTS, blank=True, null=True)

    class Meta:
        unique_together = (("node", "port"),)

    def __str__(self):
        return "{}".format(self.email)
