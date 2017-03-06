from __future__ import unicode_literals

import uuid as uuid

from django.db import models


class Node(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4,
                            editable=False)
    private_ip = models.GenericIPAddressField(protocol="IPv4", blank=False)
    ec2_id = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return "{}: {}".format(
            self.private_ip, self.ec2_id
        )

class JupyterUser(models.Model):
    PORTS = (
        ("PORT_50001", '50001'),
        ("PORT_50002", '50002'),
        ("PORT_50003", '50003'),
        ("PORT_50004", '50004')
    )

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4,
                            editable=False)
    email = models.EmailField(unique=True)
    node = models.ForeignKey(Node)
    port = models.CharField(max_length=10, choices=PORTS, blank=False,
                            default="PORT_50001")

    class Meta:
        unique_together = (("node", "port"),)

    def __str__(self):
        return "{}".format(self.email)

    def get_ebs_volume(self):
        pass
