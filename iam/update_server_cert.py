import boto3


# Create IAM client
iam = boto3.client('iam')

# Update the name of the server certificate
iam.update_server_certificate(
    ServerCertificateName='CERTIFICATE_NAME',
    NewServerCertificateName='NEW_CERTIFICATE_NAME'
)