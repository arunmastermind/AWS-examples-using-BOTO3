import boto3


# Create IAM client
iam = boto3.client('iam')

# Update access key to be active
iam.update_access_key(
    AccessKeyId='ACCESS_KEY_ID',
    Status='Active',
    UserName='IAM_USER_NAME'
)