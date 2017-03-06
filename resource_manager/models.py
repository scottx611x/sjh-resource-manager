from __future__ import unicode_literals

import uuid as uuid

from django.db import models


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


class CustomUser(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4,
                            editable=False)
    email = models.EmailField(unique=True)

    objects = UserManager()

    def __str__(self):
        return "{}".format(self.email)

    def get_ebs_volume(self):
        pass


class NodeManager(models.Manager):
    def add_user(self, user_instance):
        self.model.users.add(user_instance)

    def remove_user(self, user_instance):
        self.model.users.remove(user_instance)


class Node(models.Model):
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4,
                            editable=False)
    ip = models.GenericIPAddressField(protocol="IPv4")
    port = models.IntegerField()
    users = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return "{}:{} - {}".format(
            self.ip, self.port, self.users.all()
        )
