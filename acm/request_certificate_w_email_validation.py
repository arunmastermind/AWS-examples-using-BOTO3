import boto3


# Create ACM client
acm = boto3.client('acm')

# Request a certificate with the specified Subjects and use EMAIL validation.
response = acm.request_certificate(
    DomainName='example.com',
    ValidationMethod='EMAIL',
    SubjectAlternativeNames=[
        '*.example.com',
        '*.subdomain1.example.com',
        '*.subdomain2.example.com',
    ],
    IdempotencyToken='Token201809031516',
    DomainValidationOptions=[
        {
            'DomainName': '*.subdomain1.example.com',
            'ValidationDomain': 'example.com'
        },
        {
            'DomainName': '*.subdomain2.example.com',
            'ValidationDomain': 'example.com'
        },
    ],
    Options={
        'CertificateTransparencyLoggingPreference': 'ENABLED'
    },
)

print(response)