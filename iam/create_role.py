import boto3, json

# Create IAM client
iam = boto3.client('iam')

path='/'
role_name='TestRole1'
description='A test Role'

trust_policy={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

tags=[
    {
        'Key': 'Environment',
        'Value': 'Production'
    }
]

try:
    response = iam.create_role(
        Path=path,
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description=description,
        MaxSessionDuration=3600,
        Tags=tags
    )

    print(response)
except Exception as e:
    print(e)