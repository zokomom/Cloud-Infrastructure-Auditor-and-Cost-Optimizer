import boto3


def get_unattached_volumes():
    session = boto3.Session()

    ec2 = session.client("ec2")

    response = ec2.describe_volumes(
        Filters=[
            {
                "Name": "status",
                "Values": ["available"]
            }
        ]
    )

    return response["Volumes"]