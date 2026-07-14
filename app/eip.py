import boto3
from botocore.exceptions import ClientError


def get_unassociated_eips():

    session = boto3.Session()
    ec2 = session.client("ec2")

    try:
        response = ec2.describe_addresses()

        unused_addresses = []

        for address in response["Addresses"]:
            if "AssociationId" not in address:
                unused_addresses.append(address)

        return unused_addresses

    except ClientError as e:
        raise RuntimeError(
            f"Failed to scan Elastic IPs: {e.response['Error']['Message']}"
        )
