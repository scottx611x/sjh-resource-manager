import boto3

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

def describe_ec2():
    print ec2_client.describe_instances()

def start_ec2(ec2_id):
    ec2_client.instances.filter(InstanceIds=ec2_id).start()

def stop_ec2(ec2_id):
    ec2_client.instances.filter(InstanceIds=ec2_id).stop()

def attach_ebs(user_volume_id, ec2_to_attach_to):
    volume = main_ec2.Volume(user_volume_id)
    response = volume.attach_to_instance(
        InstanceId=ec2_to_attach_to,
        Device='string'
    )

def detach_ebs(user_volume_id, ec2_to_detach_from):
    volume = main_ec2.Volume(user_volume_id)
    response = volume.detach_from_instance(
        InstanceId=ec2_to_detach_from,
        Device='string'
    )

def ip_for_user(email, user_volume_name):
    ec2_client.instances.filter()



