import json
import boto3
from botocore.exceptions import ClientError

# Set this value before running the program
# Policy to create a new version of
policy_arn = 'arn:aws:iam::123456789012:policy/POLICY_NAME'

# Define the new version of the policy
new_policy = {
    'Version': '2012-10-17',
    'Statement': [
        {
            'Sid': 'Statement1',
            'Effect': 'Allow',
            'Action': 'EC2:*',
            'Resource': '*'
        },
        {
            'Sid': 'Statement2',
            'Effect': 'Allow',
            'Action': 'S3:*',
            'Resource': '*'
        }
    ]
}
print(f'Creating new version of IAM policy {policy_arn}')
print(json.dumps(new_policy))

# Create the new version of the policy and set it as the default version
try:
    iam = boto3.client('iam')
    response = iam.create_policy_version(PolicyArn=policy_arn,
                                         PolicyDocument=json.dumps(new_policy),
                                         SetAsDefault=True)

    print(f'Policy Version Created: {response["PolicyVersion"]["VersionId"]}')
except ClientError as e:
    print(e)