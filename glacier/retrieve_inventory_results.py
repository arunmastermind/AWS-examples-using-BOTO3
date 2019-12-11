import json
import logging
import boto3
from botocore.exceptions import ClientError


def retrieve_inventory_results(vault_name, job_id):
    """Retrieve the results of an Amazon Glacier inventory-retrieval job

    :param vault_name: string
    :param job_id: string. The job ID was returned by Glacier.Client.initiate_job()
    :return: Dictionary containing the results of the inventory-retrieval job.
    If error, return None.
    """

    # Retrieve the job results
    glacier = boto3.client('glacier')
    try:
        response = glacier.get_job_output(vaultName=vault_name, jobId=job_id)
    except ClientError as e:
        logging.error(e)
        return None

    # Read the streaming results into a dictionary
    return json.loads(response['body'].read())


def main():
    """Exercise retrieve_inventory_result()"""

    # Assign these values before running the program
    test_vault_name = 'VAULT_NAME'
    test_job_id = 'JOB_ID'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve the job results
    inventory = retrieve_inventory_results(test_vault_name, test_job_id)
    if inventory is not None:
        # Output some of the inventory information
        logging.info(f'Vault ARN: {inventory["VaultARN"]}')
        for archive in inventory['ArchiveList']:
            logging.info(f'  Size: {archive["Size"]:6d}  '
                         f'Archive ID: {archive["ArchiveId"]}')


if __name__ == '__main__':
    main()
