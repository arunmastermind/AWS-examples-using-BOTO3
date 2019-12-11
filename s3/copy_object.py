import logging
import boto3
from botocore.exceptions import ClientError


def copy_object(src_bucket_name, src_object_name,
                dest_bucket_name, dest_object_name=None):
    """Copy an Amazon S3 bucket object

    :param src_bucket_name: string
    :param src_object_name: string
    :param dest_bucket_name: string. Must already exist.
    :param dest_object_name: string. If dest bucket/object exists, it is
    overwritten. Default: src_object_name
    :return: True if object was copied, otherwise False
    """

    # Construct source bucket/object parameter
    copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
    if dest_object_name is None:
        dest_object_name = src_object_name

    # Copy the object
    s3 = boto3.client('s3')
    try:
        s3.copy_object(CopySource=copy_source, Bucket=dest_bucket_name,
                       Key=dest_object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise copy_object()"""

    # Assign these values before running the program
    src_bucket_name = 'SRC_BUCKET_NAME'
    src_object_name = 'SRC_OBJECT_NAME'
    dest_bucket_name = 'DEST_BUCKET_NAME'
    dest_object_name = 'DEST_OBJECT_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Copy the object
    success = copy_object(src_bucket_name, src_object_name,
                         dest_bucket_name, dest_object_name)
    if success:
        logging.info(f'Copied {src_bucket_name}/{src_object_name} to '
                     f'{dest_bucket_name}/{dest_object_name}')


if __name__ == '__main__':
    main()
