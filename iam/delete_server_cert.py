import boto3


# Create IAM client
iam = boto3.client('iam')

# Delete the server certificate
iam.delete_server_certificate(
    ServerCertificateName='CERTIFICATE_NAME'
)