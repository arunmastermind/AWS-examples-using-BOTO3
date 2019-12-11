import boto3


# Create IAM client
iam = boto3.client('iam')

role_name='AccountantRole1'

tags=[
    {
        'Key': 'Department',
        'Value': 'Accounting'
    },
    {
        'Key': 'Environment',
        'Value': 'Production'
    }
]

try:
    response = iam.tag_role(
        Tags=tags,
        RoleName=role_name
    )
    print(response)
except Exception as e:
    print(e)