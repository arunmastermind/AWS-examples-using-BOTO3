import boto3


# Create IAM client
iam = boto3.client('iam')

# Get the server certificate
response = iam.get_server_certificate(ServerCertificateName='CERTIFICATE_NAME')
print(response['ServerCertificate'])