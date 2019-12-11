"""Lists the items in an Amazon S3 bucket"""
import logging
import sys
import boto3
from botocore.exceptions import ClientError


def list_bucket_objects(bucket_name):
    """List the objects in an Amazon S3 bucket

    :param bucket_name: string
    :return: List of bucket objects. If error, return None.
    """

    # Retrieve the list of bucket objects
    s_3 = boto3.client('s3')
    try:
        response = s_3.list_objects_v2(Bucket=bucket_name)
    except ClientError as e:
        # AllAccessDisabled error == bucket not found
        logging.error(e)
        return None

    # Only return the contents if we found some keys
    if response['KeyCount'] > 0:
        return response['Contents']

    return None

def main():
    """Exercise list_bucket_objects()"""

    # Make sure we get a bucket name from the command line
    arguments = len(sys.argv) - 1

    if arguments < 1:
        print("You must supply a bucket name")
        return

    # Assign this value before running the program
    bucket_name = sys.argv[1]

    # Set up logging
    logging.basicConfig(level=logging.INFO,
                        format='%(message)s')

    # Retrieve the bucket's objects
    objects = list_bucket_objects(bucket_name)
    if objects is not None:
        # List the object names
        logging.info(f'Objects in {bucket_name}')
        for obj in objects:
            logging.info(f'  {obj["Key"]}')
    else:
        # Didn't get any keys
        logging.info(f'No objects in {bucket_name}')

if __name__ == '__main__':
    main()
