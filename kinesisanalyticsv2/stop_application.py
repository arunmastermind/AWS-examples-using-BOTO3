"""
Usage: python stop_application.py appname
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

    # Stop the Application
    try:
        RESP = CLIENT.stop_application(
            ApplicationName=APPLICATION_NAME
        )
        print(RESP)
    except ClientError as client_error:
        print("Got the following error calling stop_application: {}".format(client_error))
