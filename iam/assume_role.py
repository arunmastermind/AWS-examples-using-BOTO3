import boto3

# Create an STS client
sts_client = boto3.client('sts')

# Assume a role defined on an external account. The role specifies the
# permissions that are allowed on the account.
# Replace EXTERNAL_ACCOUNT_NUMBER with the account number of the external
# account.
# Replace ROLE_NAME with the name of the role defined on the external account.
# Optional, but recommended: Specify a unique ExternalId= string assigned by
# the external account.
response = sts_client.assume_role(RoleArn='arn:aws:iam::EXTERNAL_ACCOUNT_NUMBER:role/ROLE_NAME',
                                  RoleSessionName='AssumeRoleSession1')

# Reference the temporary credentials section of the response
tempCredentials = response['Credentials']

# Use the temporary credentials to create an S3 resource that can access the
# external account. The assumed role's permissions must allow the desired S3
# access.
s3_resource = boto3.resource('s3',
                             aws_access_key_id=tempCredentials['AccessKeyId'],
                             aws_secret_access_key=tempCredentials['SecretAccessKey'],
                             aws_session_token=tempCredentials['SessionToken'])

# Use the S3 resource to list the external account's buckets.
for bucket in s3_resource.buckets.all():
    print(bucket.name)