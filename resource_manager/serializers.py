from rest_framework import serializers

from .models import JupyterUser, JupyterNode


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JupyterNode
        exclude = ["id",]


class JupyterUserSerializer(serializers.ModelSerializer):
    node = NodeSerializer(required=False)
    email = serializers.EmailField(required=False)
    port = serializers.CharField(required=False)
    ebs_volume_id = serializers.CharField(required=False)

    class Meta:
        model = JupyterUser
        fields = "__all__"

    def validate(self, data):
        return data
