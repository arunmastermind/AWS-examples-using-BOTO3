import boto3


# Create ACM client
acm = boto3.client('acm')

# Request a certificate with the specified Subjects and use DNS validation.
response = acm.request_certificate(
    DomainName='example.com',
    ValidationMethod='DNS',
    SubjectAlternativeNames=[
        '*.example.com',
    ],
    IdempotencyToken='Token201809031515',
    Options={
        'CertificateTransparencyLoggingPreference': 'ENABLED'
    }
)

print(response)