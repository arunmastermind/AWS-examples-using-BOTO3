import logging
import boto3
from botocore.exceptions import ClientError


def describe_job(vault_name, job_id):
    """Retrieve the status of an Amazon S3 Glacier job, such as an
    inventory-retrieval job

    To retrieve the output of the finished job, call Glacier.Client.get_job_output()

    :param vault_name: string
    :param job_id: string. The job ID was returned by Glacier.Client.initiate_job().
    :return: Dictionary of information related to the job. If error, return None.
    """

    # Retrieve the status of the job
    glacier = boto3.client('glacier')
    try:
        response = glacier.describe_job(vaultName=vault_name, jobId=job_id)
    except ClientError as e:
        logging.error(e)
        return None
    return response


def main():
    """Exercise describe_job()"""

    # Assign the following values before running the program
    test_vault_name = 'VAULT_NAME'
    test_job_id = 'JOB_ID'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the job's status
    response = describe_job(test_vault_name, test_job_id)
    if response is not None:
        logging.info(f'Job Type: {response["Action"]}, '
                     f'Status: {response["StatusCode"]}')


if __name__ == '__main__':
    main()
