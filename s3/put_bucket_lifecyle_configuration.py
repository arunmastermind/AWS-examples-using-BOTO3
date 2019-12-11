import logging
import boto3
from botocore.exceptions import ClientError

# Lifecycle configuration settings
# The optional ID can be any descriptive string.
# The empty Prefix setting causes all objects in the bucket to transition.
# The 0 Days setting causes the transition to occur "immediately" (or within
# a short time period, less than one day)
lifecycle_config_settings = {
    'Rules': [
        {'ID': 'S3 Glacier Transition Rule',
         'Filter': {'Prefix': ''},
         'Status': 'Enabled',
         'Transitions': [
             {'Days': 0,
              'StorageClass': 'GLACIER'}
         ]}
    ]}


def put_bucket_lifecycle_configuration(bucket_name, lifecycle_config):
    """Set the lifecycle configuration of an Amazon S3 bucket

    :param bucket_name: string
    :param lifecycle_config: dict of lifecycle configuration settings
    :return: True if lifecycle configuration was set, otherwise False
    """

    # Set the configuration
    s3 = boto3.client('s3')
    try:
        s3.put_bucket_lifecycle_configuration(Bucket=bucket_name,
                                              LifecycleConfiguration=lifecycle_config)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise put_bucket_lifecycle_configuration()"""

    # Assign this value before running the program
    test_bucket_name = 'BUCKET_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Set the bucket's lifecycle configuration
    success = put_bucket_lifecycle_configuration(test_bucket_name,
                                                 lifecycle_config_settings)

    if success:
        logging.info(f'The lifecycle configuration was set for {test_bucket_name}')


if __name__ == '__main__':
    main()
