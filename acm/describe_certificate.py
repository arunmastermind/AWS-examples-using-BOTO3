import boto3


# Create ACM client
acm = boto3.client('acm')

# Describe the specified certificate.
response = acm.describe_certificate(
    CertificateArn='arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012'
)
print(response)