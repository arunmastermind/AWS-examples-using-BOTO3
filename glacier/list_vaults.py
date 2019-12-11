import logging
import boto3


def list_vaults(max_vaults=10, iter_marker=None):
    """List Amazon S3 Glacier vaults owned by the AWS account

    :param max_vaults: Maximum number of vaults to retrieve
    :param iter_marker: Marker used to identify start of next batch of vaults
    to retrieve
    :return: List of dictionaries containing vault information
    :return: String marking the start of next batch of vaults to retrieve.
    Pass this string as the iter_marker argument in the next invocation of
    list_vaults().
    """

    # Retrieve vaults
    glacier = boto3.client('glacier')
    if iter_marker is None:
        vaults = glacier.list_vaults(limit=str(max_vaults))
    else:
        vaults = glacier.list_vaults(limit=str(max_vaults), marker=iter_marker)
    marker = vaults.get('Marker')       # None if no more vaults to retrieve
    return vaults['VaultList'], marker


def main():
    """Exercise list_vaults()"""

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # List the vaults
    vaults, marker = list_vaults()
    while True:
        # Print info about retrieved vaults
        for vault in vaults:
            logging.info(f'{vault["NumberOfArchives"]:3d}  '
                         f'{vault["SizeInBytes"]:12d}  {vault["VaultName"]}')

        # If no more vaults exist, exit loop, otherwise retrieve the next batch
        if marker is None:
            break
        vaults, marker = list_vaults(iter_marker=marker)


if __name__ == '__main__':
    main()
