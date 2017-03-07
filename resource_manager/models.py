from __future__ import unicode_literals

import uuid as uuid

from django.db import models


class Node(models.Model):
    private_ip = models.GenericIPAddressField(protocol="IPv4", blank=True,
                                              null=True)
    ec2_id = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        unique_together = (("private_ip", "ec2_id"),)

    def __str__(self):
        return "{}: {}".format(
            self.private_ip, self.ec2_id
        )

class JupyterUser(models.Model):
    PORTS = (
        ("50001", '50001'),
        ("50002", '50002'),
        ("50003", '50003'),
        ("50004", '50004'),
        ("50005", '50005'),
        ("50006", '50006'),
        ("50007", '50007')
    )

    email = models.EmailField(unique=True, primary_key=True)
    node = models.ForeignKey(Node, blank=True, null=True)
    port = models.CharField(max_length=5, choices=PORTS, blank=True, null=True)

    class Meta:
        unique_together = (("node", "port"),)

    def __str__(self):
        return "{}".format(self.email)

    def get_ebs_volume(self):
        pass
