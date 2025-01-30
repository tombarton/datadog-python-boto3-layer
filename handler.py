import importlib.util

if importlib.util.find_spec("unzip_requirements"):
    import unzip_requirements  # type: ignore # noqa: F401

import botocore

print("botocore.__version__", botocore.__version__)

import boto3

print("boto3.__version__", boto3.__version__)


def hello(event, context):
    client = boto3.client("s3")
    buckets = client.list_buckets()

    for bucket in buckets["Buckets"]:
        print(bucket["Name"])
