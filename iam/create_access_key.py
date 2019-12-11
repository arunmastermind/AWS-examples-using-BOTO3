import boto3

# Create IAM client
iam = boto3.client('iam')

# Create an access key
response = iam.create_access_key(
    UserName='IAM_USER_NAME'
)

print(response['AccessKey'])