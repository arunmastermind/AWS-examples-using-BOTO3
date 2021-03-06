import logging
import boto3
from botocore.exceptions import ClientError


def get_bucket_lifecycle_configuration(bucket_name):
    """Retrieve the lifecycle configuration of an Amazon S3 bucket

    :param bucket_name: string
    :return: List of lifecycle configuration rules. If no configuration is
     defined, the list is empty. If error, returns None.
    """

    # Retrieve the configuration
    s3 = boto3.client('s3')
    try:
        response = s3.get_bucket_lifecycle_configuration(Bucket=bucket_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchLifecycleConfiguration':
            return []
        else:
            # e.response['Error']['Code'] == 'NoSuchBucket', etc.
            logging.error(e)
            return None
    return response['Rules']


def main():
    """Exercise get_bucket_lifecycle_configuration()"""

    # Assign this value before running the program
    test_bucket_name = 'BUCKET_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the lifecycle configuration
    lifecycle_config = get_bucket_lifecycle_configuration(test_bucket_name)
    if lifecycle_config is not None:
        if not lifecycle_config:
            logging.info(f'{test_bucket_name} does not have a lifecycle configuration.')
        else:
            for rule in lifecycle_config:
                logging.info(f'Rule: {rule["ID"]}, Status: {rule["Status"]}')
                for transition in rule['Transitions']:
                    logging.info(f'--After {transition["Days"]:3d} days, '
                                 f'transition to storage class '
                                 f'{transition["StorageClass"]}')


if __name__ == '__main__':
    main()
