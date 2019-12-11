import boto3


# Create IAM client
iam = boto3.client('iam')

# Get last use of access key
response = iam.get_access_key_last_used(
    AccessKeyId='ACCESS_KEY_ID'
)

print(response['AccessKeyLastUsed'])