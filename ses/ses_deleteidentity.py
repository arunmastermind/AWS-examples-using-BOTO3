import boto3

# Delete the specified identity
ses = boto3.client('ses')
response = ses.delete_identity(Identity='DOMAIN_NAME')
print(response)
