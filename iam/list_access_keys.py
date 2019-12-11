import boto3

# Create IAM client
iam = boto3.client('iam')

# List access keys through the pagination interface.
paginator = iam.get_paginator('list_access_keys')
for response in paginator.paginate(UserName='IAM_USER_NAME'):
    print(response)