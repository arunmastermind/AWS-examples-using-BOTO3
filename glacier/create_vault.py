import logging
import boto3
from botocore.exceptions import ClientError


def create_vault(vault_name):
    """Create an Amazon Glacier vault.

    :param vault_name: string
    :return: glacier.Vault object if vault was created, otherwise None
    """

    glacier = boto3.resource('glacier')
    try:
        vault = glacier.create_vault(vaultName=vault_name)
    except ClientError as e:
        logging.error(e)
        return None
    return vault


def main():
    """ Exercise create_vault()"""

    # Assign this value before running the program
    test_vault_name = 'VAULT_NAME'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Create the Glacier vault
    vault = create_vault(test_vault_name)
    if vault is not None:
        logging.info(f'Created vault {vault.name}')


if __name__ == '__main__':
    main()
