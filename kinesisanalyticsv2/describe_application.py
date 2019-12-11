"""
Usage: python describe_application.py appname
"""

import sys
import boto3

from botocore.exceptions import ClientError

ARGUMENTS = len(sys.argv) - 1

if ARGUMENTS < 1:
    print("You must supply an application name")

else:
    APPLICATION_NAME = sys.argv[1]

    # Create kinesisanalyticsv2 client
    CLIENT = boto3.client('kinesisanalyticsv2')

    # Describe the Application details
    try:
        RESP = CLIENT.describe_application(
            ApplicationName=APPLICATION_NAME
        )
        print(RESP)
    except ClientError as client_error:
        print("Got the following error calling describe_application: {}".format(client_error))