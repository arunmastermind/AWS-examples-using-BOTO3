import logging
import boto3
from botocore.exceptions import ClientError


def delete_objects(bucket_name, object_names):
    """Delete multiple objects from an Amazon S3 bucket

    :param bucket_name: string
    :param object_names: list of strings
    :return: True if the referenced objects were deleted, otherwise False
    """

    # Convert list of object names to appropriate data format
    objlist = [{'Key': obj} for obj in object_names]

    # Delete the objects
    s3 = boto3.client('s3')
    try:
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objlist})
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise delete_objects()"""

    # Assign these values before running the program
    test_bucket_name = 'BUCKET_NAME'
    test_object_names = ['OBJECT_NAME_01', 'OBJECT_NAME_02']

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Delete the objects
    if delete_objects(test_bucket_name, test_object_names):
        logging.info(f'Multiple objects were deleted from {test_bucket_name}')


if __name__ == '__main__':
    main()
