import boto3


# Create ACM client
acm = boto3.client('acm')

# Add tag(s) to the specified certificate.
response = acm.add_tags_to_certificate(
    CertificateArn='arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012',
    Tags=[
        {
            'Key': 'TagKey1',
            'Value': 'TagValue1'
        },
        {
            'Key': 'TagKey2',
            'Value': 'TagValue2'
        },
    ]
)

print(response)
