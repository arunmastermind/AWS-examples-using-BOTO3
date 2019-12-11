import logging
import boto3
from botocore.exceptions import ClientError


def upload_archive(vault_name, src_data):
    """Add an archive to an Amazon S3 Glacier vault.

    The upload occurs synchronously.

    :param vault_name: string
    :param src_data: bytes of data or string reference to file spec
    :return: If src_data was added to vault, return dict of archive
    information, otherwise None
    """

    # The src_data argument must be of type bytes or string
    # Construct body= parameter
    if isinstance(src_data, bytes):
        object_data = src_data
    elif isinstance(src_data, str):
        try:
            object_data = open(src_data, 'rb')
            # possible FileNotFoundError/IOError exception
        except Exception as e:
            logging.error(e)
            return None
    else:
        logging.error('Type of ' + str(type(src_data)) +
                      ' for the argument \'src_data\' is not supported.')
        return None

    glacier = boto3.client('glacier')
    try:
        archive = glacier.upload_archive(vaultName=vault_name,
                                         body=object_data)
    except ClientError as e:
        logging.error(e)
        return None
    finally:
        if isinstance(src_data, str):
            object_data.close()

    # Return dictionary of archive information
    return archive


def main():
    """Exercise upload_archive()"""

    # Assign these values before running the program
    test_vault_name = 'VAULT_NAME'
    filename = 'C:\\path\\to\\filename.ext'
    # Alternatively, specify object contents using bytes.
    # filename = b'This is the data to store in the Glacier archive.'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Upload the archive
    archive = upload_archive(test_vault_name, filename)
    if archive is not None:
        logging.info(f'Archive {archive["archiveId"]} added to {test_vault_name}')


if __name__ == '__main__':
    main()
