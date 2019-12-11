import boto3


# Create ACM client
acm = boto3.client('acm')

# List certificates with the pagination interface
paginator = acm.get_paginator('list_certificates')
for response in paginator.paginate():
    for certificate in response['CertificateSummaryList']:
        print(certificate)