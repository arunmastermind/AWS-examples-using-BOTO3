import boto3


# Create ACM client
acm = boto3.client('acm')

# List certificates with the pagination interface
paginator = acm.get_paginator('list_certificates')
for response in paginator.paginate(
Includes={
        'extendedKeyUsage': [
            'TLS_WEB_SERVER_AUTHENTICATION','TLS_WEB_CLIENT_AUTHENTICATION','CODE_SIGNING','EMAIL_PROTECTION','TIME_STAMPING','OCSP_SIGNING','IPSEC_END_SYSTEM','IPSEC_TUNNEL','IPSEC_USER','ANY','NONE'
        ],
        'keyUsage': [
            'DIGITAL_SIGNATURE','NON_REPUDIATION','KEY_ENCIPHERMENT','DATA_ENCIPHERMENT','KEY_AGREEMENT','CERTIFICATE_SIGNING','CRL_SIGNING','ENCIPHER_ONLY','DECIPHER_ONLY','ANY','CUSTOM',
        ],
        'keyTypes': [
            'RSA_2048','RSA_1024','RSA_4096','EC_prime256v1','EC_secp384r1','EC_secp521r1'
        ]
    }
):
    for certificate in response['CertificateSummaryList']:
        print(certificate)

