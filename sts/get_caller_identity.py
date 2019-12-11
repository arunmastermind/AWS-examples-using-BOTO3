import boto3

# Create IAM client
sts = boto3.client('sts')

identity = sts.get_caller_identity()

print('Default Credential Provider Chain Identity: ' + identity['Arn'])