import logging
import boto3
from botocore.exceptions import ClientError


def delete_archive(vault_name, archive_id):
    """Delete an archive from an Amazon S3 Glacier vault

    :param vault_name: string
    :param archive_id: string
    :return: True if archive was deleted, otherwise False
    """

    # Delete the archive
    glacier = boto3.client('glacier')
    try:
        response = glacier.delete_archive(vaultName=vault_name,
                                          archiveId=archive_id)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise delete_vault()"""

    # Assign these values before running the program
    test_vault_name = 'VAULT_NAME'
    test_archive_id = 'ARCHIVE_ID'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Delete the archive
    success = delete_archive(test_vault_name, test_archive_id)
    if success:
        logging.info(f'Deleted archive {test_archive_id} from {test_vault_name}')


if __name__ == '__main__':
    main()
