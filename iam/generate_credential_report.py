import boto3

# Create IAM client
client = boto3.client('iam')

# Generate credentials report of all users in account
response = client.generate_credential_report()

print(response)