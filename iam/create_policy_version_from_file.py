import boto3
from botocore.exceptions import ClientError

# Assign these values before running the program
policy_arn = 'arn:aws:iam::123456789012:policy/POLICY_NAME'
policy_file_name = 'POLICY_FILENAME.JSON'

try:
    # Read the policy definition from a file
    with open(policy_file_name, 'r') as f:
        policy_version = f.read()

    # Show the loaded policy definition
    print(f'Creating new version of IAM policy {policy_arn}')
    print(policy_version)

    # Create a new version of the policy and set it as the default version
    iam = boto3.client('iam')
    response = iam.create_policy_version(PolicyArn=policy_arn,
                                         PolicyDocument=policy_version,
                                         SetAsDefault=True)

    print(f'Policy Version Created: {response["PolicyVersion"]["VersionId"]}')
except ClientError as e:
    print(e)
