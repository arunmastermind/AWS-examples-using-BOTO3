import boto3


# Create IAM client
iam = boto3.client('iam')

# Update a user name
iam.update_user(
    UserName='IAM_USER_NAME',
    NewUserName='NEW_IAM_USER_NAME'
)