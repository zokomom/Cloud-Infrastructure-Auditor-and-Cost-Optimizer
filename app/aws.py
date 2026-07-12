import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def get_session():
    return boto3.Session()


def get_caller_identity():
    try:
        session = get_session()
        sts = session.client("sts")
        return sts.get_caller_identity()
    except (NoCredentialsError, ClientError):
        return None


def get_region():
    session = get_session()
    return session.region_name


def get_profile():
    session = get_session()
    return session.profile_name or "default"
