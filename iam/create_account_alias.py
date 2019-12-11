import boto3

# Create IAM client
iam = boto3.client('iam')

# Create an account alias
iam.create_account_alias(
    AccountAlias='ALIAS'
)