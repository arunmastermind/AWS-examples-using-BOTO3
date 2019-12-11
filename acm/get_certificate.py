import boto3


# Create ACM client
acm = boto3.client('acm')

try:
    # Describe the specified certificate.
    response = acm.get_certificate(
        CertificateArn='arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012'
    )

    print('\n\rCertificate:\n\r')
    print(response['Certificate'])
    print('CertificateChain:\n\r')
    print(response['CertificateChain'])

except acm.exceptions.ResourceNotFoundException as e:
    print(e.response['Error']['Code'] + ': ' + e.response['Error']['Message'])
    exit(1)

except acm.exceptions.RequestInProgressException as e:
    print(e.response['Error']['Code'] + ': ' + e.response['Error']['Message'])
    exit(1)

except:
    print('There was an error.')
    exit(1)

