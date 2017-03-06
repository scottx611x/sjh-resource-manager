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


class UserManager(models.Manager):
    def create_user(self, email):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.save(using=self._db)
        return user

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the address by lowercasing the domain part of the email
        address.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email


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

    objects = UserManager()

    class Meta:
        unique_together = (("node", "port"),)

    def __str__(self):
        return "{}".format(self.email)

    def get_ebs_volume(self):
        pass
