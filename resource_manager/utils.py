import boto3
import paramiko
import time

from django.conf import settings

from resource_manager.models import JupyterNode, JupyterUser

ec2_client = boto3.client('ec2')


def get_fullest_node():
    fullest_node = None
    total = 0
    for node in JupyterNode.objects.all():
        total_users = JupyterUser.objects.filter(node=node).count()
        if total <= total_users < 4:
            fullest_node = node
    return fullest_node


def create_ebs_volume():
    response = ec2_client.create_volume(
        DryRun=False,
        Size=1,
        AvailabilityZone='us-east-1a',
        VolumeType='standard',
        Encrypted=False
    )
    waiter = ec2_client.get_waiter('volume_available')
    waiter.wait(
        DryRun=False,
        VolumeIds=[
            response["VolumeId"],
        ],
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available',
                ]
            },
        ]
    )
    return response["VolumeId"]


def attach_ebs_volume(ebs_id, ec2_id, special_device):
    ec2_client.attach_volume(
        DryRun=False,
        VolumeId=ebs_id,
        InstanceId=ec2_id,
        Device=special_device
    )
    waiter = ec2_client.get_waiter('instance_exists')
    try:
        waiter.wait(
            DryRun=False,
            InstanceIds=[ec2_id],
            Filters=[
                {
                    'Name': 'block-device-mapping.status',
                    'Values': [
                        'attached',
                    ]
                },
            ]
        )
    except Exception as e:
        print e
        return False
    else:
        return True


def mount_linux_device(ec2_pub_dns, username, v_dev, volume_path):
    ssh = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(settings.PKEY)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ec2_pub_dns, username=username, pkey=key)

    stdin, stdout, stderr = ssh.exec_command("sudo mkdir -p {}".format(volume_path))
    stdout = stdout.readlines()
    stderr = stderr.readlines()

    stdin, stdout, stderr = ssh.exec_command(
        "sudo yes | sudo mkfs -t ext3 {}".format( v_dev.replace("/sd", "/xvd"))
    )
    stdout = stdout.readlines()
    stderr = stderr.readlines()

    stdin, stdout, stderr = ssh.exec_command(
        "sudo mount {} {}".format(v_dev.replace("/sd", "/xvd"), volume_path))
    stdout = stdout.readlines()
    stderr = stderr.readlines()

    ssh.close()


def describe_ec2():
    print ec2_client.describe_instances()


def start_ec2(ec2_id):
    ec2_client.instances.filter(InstanceIds=[ec2_id]).start()


def stop_ec2(ec2_id):
    ec2_client.instances.filter(InstanceIds=[ec2_id]).stop()


def detach_ebs(ebs_id, ec2_id, special_device):
    ec2_client.attach_volume(
        DryRun=False,
        VolumeId=ebs_id,
        InstanceId=ec2_id,
        Device=special_device
    )
    waiter = ec2_client.get_waiter('instance_exists')
    try:
        waiter.wait(
            DryRun=False,
            InstanceIds=[ec2_id],
            Filters=[
                {
                    'Name': 'block-device-mapping.status',
                    'Values': [
                        'detached',
                    ]
                },
            ]
        )
    except Exception as e:
        print e
        return False
    else:
        return True
