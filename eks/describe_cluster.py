import boto3


def describe_cluster(cluster_name):
    """Retrieve information about an Amazon EKS cluster

    :param cluster_name: string
    :return: Dictionary containing information of cluster. If error, return None.
    """

    eks = boto3.client('eks')

    try:
        response = eks.describe_cluster(name=cluster_name)
    except Exception as e:
        # e.response['Error']['Code'] == 'ResourceNotFoundException'
        return None
    return response['cluster']


def main():
    test_cluster_name = 'test-cluster-name'

    result = describe_cluster(test_cluster_name)
    if result is None:
        print('ERROR: Could not retrieve information about cluster {}'.format(test_cluster_name))
    else:
        print('Cluster Name: {}'.format(result['name']))
        print('Status: {}'.format(result['status']))
        # Some information is not available until after the cluster has been created
        if result['status'] != 'CREATING':
            print('ARN: {}'.format(result['arn']))
            print('Endpoint: {}'.format(result['endpoint']))
            print('Certificate Authority (truncated): {}...'.format(result['certificateAuthority']['data'][:40]))


if __name__ == '__main__':
    main()