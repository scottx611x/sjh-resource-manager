import boto3
from django.conf import settings
from django.db import transaction, IntegrityError
from django.http import HttpResponseServerError
from rest_framework import viewsets
from rest_framework.response import Response

from resource_manager.models import JupyterUser
from resource_manager.serializers import JupyterUserSerializer
from resource_manager.utils import get_fullest_node, create_ebs_volume, \
    attach_ebs_volume, mount_linux_device


class JupyterUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = JupyterUser.objects.all()
    serializer_class = JupyterUserSerializer
    lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
    lookup_field = "email"
    http_method_names = ["get", "put"]
    ec2_client = boto3.client('ec2')

    def get_object(self):
        if self.request.method == 'PUT':
            try:
                JupyterUser.objects.get(
                    email=self.kwargs.get('email')
                )
            except JupyterUser.MultipleObjectsReturned:
                return HttpResponseServerError()
            except JupyterUser.DoesNotExist:
                data = {
                    "email": self.kwargs.get('email'),
                    "volume_name": self.request.query_params["volume"]
                }

                jupyter_user = JupyterUser(
                    email=self.kwargs.get('email'),
                    volume_name=self.request.query_params["volume"]
                )
                serializer = self.serializer_class(jupyter_user, data=data)
                if serializer.is_valid():
                    serializer.save()
                    node = get_fullest_node()
                    jupyter_user.node = node
                    jupyter_user.save()

                    sys_devices = {
                        "50001": "/dev/sdh",
                        "50002": "/dev/sdi",
                        "50003": "/dev/sdj",
                        "50004": "/dev/sdk"
                    }
                    for port in ["50001", "50002", "50003", "50004"]:
                        try:
                            jupyter_user.port = port
                            with transaction.atomic():
                                jupyter_user.save()
                        except IntegrityError:
                            continue
                        else:
                            special_device = sys_devices[port]
                            ebs_id = create_ebs_volume()
                            jupyter_user.ebs_volume_id = ebs_id
                            jupyter_user.save()

                            is_ebs_attached = attach_ebs_volume(
                                jupyter_user.ebs_volume_id,
                                jupyter_user.node.ec2_id,
                                special_device
                            )

                            jupyter_user.ebs_volume_attached = is_ebs_attached
                            jupyter_user.save()
                            ec2_info = self.ec2_client.describe_instances(
                                DryRun=False,
                                InstanceIds=[jupyter_user.node.ec2_id],
                            )
                            public_dns = ec2_info["Reservations"][0]["Instances"][0]["PublicDnsName"]

                            try:
                                mount_linux_device(
                                    public_dns,
                                    settings.OS_USERNAME,
                                    special_device,
                                    jupyter_user.volume_name
                                )
                            except Exception as e:
                                print e

                            return jupyter_user
                else:
                    return Response(serializer.errors,
                                    status=400)

            else:
                return JupyterUser.objects.get(
                    email=self.kwargs.get('email')
                )

        else:
            return super(JupyterUserViewSet, self).get_object()
