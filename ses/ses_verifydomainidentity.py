import boto3

# Add a domain to the list of identities in the AWS SES account.
# Also attempts to verify the domain.
ses = boto3.client('ses')
response = ses.verify_domain_identity(Domain='DOMAIN_NAME')
print(response)
