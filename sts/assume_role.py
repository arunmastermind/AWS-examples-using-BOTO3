import boto3

# Create IAM client
sts_default_provider_chain = boto3.client('sts')

print('Default Provider Identity: : ' + sts_default_provider_chain.get_caller_identity()['Arn'])

role_to_assume_arn='arn:aws:iam::123456789012:role/roleName'
role_session_name='test_session'

response=sts_default_provider_chain.assume_role(
    RoleArn=role_to_assume_arn,
    RoleSessionName=role_session_name
)

creds=response['Credentials']

sts_assumed_role = boto3.client('sts',
    aws_access_key_id=creds['AccessKeyId'],
    aws_secret_access_key=creds['SecretAccessKey'],
    aws_session_token=creds['SessionToken'],
)

print('AssumedRole Identity: ' + sts_assumed_role.get_caller_identity()['Arn'])