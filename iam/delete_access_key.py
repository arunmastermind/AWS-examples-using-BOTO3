import boto3

# Create IAM client
iam = boto3.client('iam')

# Delete access key
iam.delete_access_key(
    AccessKeyId='ACCESS_KEY_ID',
    UserName='IAM_USER_NAME'
)