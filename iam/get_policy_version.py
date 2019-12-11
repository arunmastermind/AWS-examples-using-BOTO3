import boto3

# Create IAM client
iam = boto3.client('iam')

policy_arn = 'arn:aws:iam::aws:policy/AWSLambdaExecute'

# Get policy
get_policy_response = iam.get_policy(
    PolicyArn=policy_arn
)

version_id = get_policy_response['Policy']['DefaultVersionId']

# Get default version of policy
get_policy_version_response = iam.get_policy_version(
    PolicyArn=policy_arn,
    VersionId=version_id,
)

policy_document = get_policy_version_response['PolicyVersion']['Document']

print("IAM Policy Version: " + policy_document['Version'])
print("Statements: ")
for statement in policy_document['Statement']:
    print(statement)

print("\n\rUnformatted Policy Document: \n\r" + str(policy_document))