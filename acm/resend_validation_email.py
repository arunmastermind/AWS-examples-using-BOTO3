import boto3


# Create ACM client
acm = boto3.client('acm')

# Resend validation email for one of the Subject or SANs of an ACM certificate.
response = acm.resend_validation_email(
    CertificateArn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012',
    Domain='*.subdomain1.example.com',
    ValidationDomain='example.com'
)

print(response)

