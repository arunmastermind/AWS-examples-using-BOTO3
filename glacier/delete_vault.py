import logging
import boto3
from botocore.exceptions import ClientError


def delete_vault(vault_name):
    """Delete an Amazon S3Glacier vault

    :param vault_name: string
    :return: True if vault was deleted, otherwise False
    """

    # Delete the vault
    glacier = boto3.client('glacier')
    try:
        response = glacier.delete_vault(vaultName=vault_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise delete_vault()"""

    # Assign this value before running the program
    test_vault_name = 'VAULT_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Delete the vault
    success = delete_vault(test_vault_name)
    if success:
        logging.info(f'Deleted vault {test_vault_name}')


if __name__ == '__main__':
    main()
