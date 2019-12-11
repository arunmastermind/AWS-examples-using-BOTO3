import boto3

# Create client
iam = boto3.client('iam')

# Get account overview summary
summary = iam.get_account_summary()
print(summary)