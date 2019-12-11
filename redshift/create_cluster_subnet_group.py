import boto3
from botocore.exceptions import ClientError


def create_redshift_cluster_subnet_group(group_name,
                                         subnet_ids,
                                         Desc='Redshift cluster subnet group'):
    """Create a subnet group for an Amazon Redshift cluster

    :param group_name: string; Name to assign to the group
    :param subnet_ids: list of strings; List of existing subnet IDs
    :param Desc: string; Description of group
    :return: dictionary containing subnet information, otherwise None
    """

    redshift_client = boto3.client('redshift')
    try:
        response = redshift_client.create_cluster_subnet_group(
            ClusterSubnetGroupName=group_name,
            SubnetIds=subnet_ids,
            Description=Desc)
    except ClientError as e:
        print(f'ERROR: {e}')
        return None
    else:
        return response['ClusterSubnetGroup']
        
def main():
    """Test create_redshift_cluster_subnet_group()"""

    subnet_group_name = 'myTestRedshiftSubnetGroup'
    subnet_ids = ['subnet-1234abcd']  # Replace with an existing subnet ID
    description = 'Demo subnet group for Amazon Redshift'

    subnet_info = create_redshift_cluster_subnet_group(subnet_group_name,
                                                       subnet_ids,
                                                       description)
    if subnet_info is not None:
        print(f'Created cluster subnet group: {subnet_info["ClusterSubnetGroupName"]}')
        print(f'VPC ID: {subnet_info["VpcId"]}')
        print(f'Subnet group status: {subnet_info["SubnetGroupStatus"]}')
        for subnet in subnet_info['Subnets']:
            print(f'Subnet ID: {subnet["SubnetIdentifier"]}')
            print(f'    Availability Zone: {subnet["SubnetAvailabilityZone"]["Name"]}')
            print(f'    Status: {subnet["SubnetStatus"]}')


if __name__ == '__main__':
    main()
