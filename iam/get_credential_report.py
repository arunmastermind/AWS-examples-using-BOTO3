import boto3

# Create IAM client
client = boto3.client('iam')
response = client.get_credential_report()
print(response)