"""
Usage: python describe_application_snapshot.py
"""

import sys
import boto3

from botocore.exceptions import ClientError

ARGUMENTS = len(sys.argv) - 1

if ARGUMENTS < 2:
    print("You must supply an application name and snapshot name")
else:
    APPLICATION_NAME = sys.argv[1]
    SNAPSHOT_NAME = sys.argv[2]

    # Create kinesisanalyticsv2 client
    CLIENT = boto3.client('kinesisanalyticsv2')

    # Describe the snapshot details
    try:
        RESP = CLIENT.describe_application_snapshot(
            ApplicationName=APPLICATION_NAME,
            SnapshotName=SNAPSHOT_NAME
        )
        print(RESP)

    except ClientError as client_error:
        print("Got the following error calling describe_application_snapshot: {}".format(client_error))