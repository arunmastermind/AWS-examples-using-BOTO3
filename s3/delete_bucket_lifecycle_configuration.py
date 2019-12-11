import logging
import boto3
from botocore.exceptions import ClientError


def delete_bucket_lifecycle_configuration(bucket_name):
    """Delete the lifecycle configuration of an Amazon S3 bucket

    :param bucket_name: string
    :return: True if bucket lifecycle configuration was deleted, otherwise
    False. Note: If the bucket does not have a lifecycle configuration, the
    method returns True.
    """

    # Delete the configuration
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket_lifecycle(Bucket=bucket_name)
    except ClientError as e:
        # e.response['Error']['Code'] == 'AllAccessDisabled' (bucket does not
        # exist), etc.
        logging.error(e)
        return False
    return True


def main():
    """Exercise delete_bucket_lifecycle_configuration"""

    # Assign this value before running the program
    test_bucket_name = 'BUCKET_NAME'
    test_bucket_name = 'scalwas-bucket-name'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Delete the configuration
    success = delete_bucket_lifecycle_configuration(test_bucket_name)
    if success:
        logging.info(f'Deleted the lifecycle configuration of {test_bucket_name}')


if __name__ == '__main__':
    main()
