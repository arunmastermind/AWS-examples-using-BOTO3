import logging
import boto3
from botocore.exceptions import ClientError


def get_bucket_cors(bucket_name):
    """Retrieve the CORS configuration rules of an Amazon S3 bucket

    :param bucket_name: string
    :return: List of the bucket's CORS configuration rules. If no CORS
    configuration exists, return empty list. If error, return None.
    """

    # Retrieve the CORS configuration
    s3 = boto3.client('s3')
    try:
        response = s3.get_bucket_cors(Bucket=bucket_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchCORSConfiguration':
            return []
        else:
            # AllAccessDisabled error == bucket not found
            logging.error(e)
            return None
    return response['CORSRules']


def main():
    """Exercise get_bucket_cors()"""

    # Assign this value before running the program
    test_bucket_name = 'BUCKET_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the CORS configuration
    cors_rules = get_bucket_cors(test_bucket_name)

    if cors_rules is not None:
        if not cors_rules:
            logging.info('Bucket does not have a CORS configuration.')
        else:
            # Output the rules
            for rule in cors_rules:
                logging.info('CORS Rule:')
                logging.info('  Allowed Origins:')
                for origin in rule['AllowedOrigins']:
                    logging.info(f'    {origin}')
                logging.info('  Allowed Methods:')
                for method in rule['AllowedMethods']:
                    logging.info(f'    {method}')


if __name__ == '__main__':
    main()
