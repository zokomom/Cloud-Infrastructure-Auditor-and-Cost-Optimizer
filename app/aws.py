import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def get_session():
    return boto3.Session()


def get_caller_identity():
    try:
        session = get_session()
        sts = session.client("sts")

        return sts.get_caller_identity()

    except NoCredentialsError:
        return None

    except ClientError:
        return None
