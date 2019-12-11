import logging
import boto3
from botocore.exceptions import ClientError


def create_presigned_url_expanded(client_method_name, method_parameters=None,
                                  expiration=3600, http_method=None):
    """Generate a presigned URL to invoke an S3.Client method

    Not all the client methods provided in the AWS Python SDK are supported.

    :param client_method_name: Name of the S3.Client method, e.g., 'list_buckets'
    :param method_parameters: Dictionary of parameters to send to the method
    :param expiration: Time in seconds for the presigned URL to remain valid
    :param http_method: HTTP method to use (GET, etc.)
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 client method
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(ClientMethod=client_method_name,
                                                    Params=method_parameters,
                                                    ExpiresIn=expiration,
                                                    HttpMethod=http_method)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    Sharing an S3 object is the intended use of S3 presigned URLs. The AWS
    Python SDK also supports generating a presigned URL to perform other S3
    operations. See the create_presigned_url_expanded() method in this file.

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def main():
    """Exercise create_presigned_url() and create_presigned_url_expanded()"""

    # Set these values before running the program
    bucket_name = 'BUCKET_NAME'
    object_name = 'OBJECT_NAME'
    expiration = 60*10          # 10 minutes

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Generate a presigned URL to share an S3 object
    url = create_presigned_url(bucket_name, object_name, expiration)
    if url is not None:
        logging.info(f'Presigned URL to share an S3 object: {url}')

    # Generate a presigned URL to list all buckets
    url = create_presigned_url_expanded('list_buckets')
    if url is not None:
        logging.info(f'Presigned URL to list all buckets: {url}')

    # Generate a presigned URL to retrieve a bucket's region
    url = create_presigned_url_expanded('get_bucket_location',
                                        {'Bucket': bucket_name})
    if url is not None:
        logging.info(f'Presigned URL to retrieve a bucket\'s region: {url}')


if __name__ == '__main__':
    main()
