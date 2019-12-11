import boto3

# Create IAM client
iam = boto3.client('iam')

account_details = iam.get_account_authorization_details()
print(account_details)