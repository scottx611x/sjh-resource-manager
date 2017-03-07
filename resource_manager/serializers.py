from rest_framework import serializers

from .models import JupyterUser, Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        exclude = ["id",]


class JupyterUserSerializer(serializers.ModelSerializer):
    node = NodeSerializer(allow_null=True)

    class Meta:
        model = JupyterUser
        fields = '__all__'
