import boto3


# Create ACM client
acm = boto3.client('acm')

# List certificate tags.
response = acm.list_tags_for_certificate(
    CertificateArn='arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012'
)
for tag in response['Tags']:
    print(tag)
