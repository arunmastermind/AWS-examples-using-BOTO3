import boto3

# Create IAM client
iam = boto3.client('iam')

# Delete an account alias
iam.delete_account_alias(
    AccountAlias='ALIAS'
)