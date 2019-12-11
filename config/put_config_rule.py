import boto3
from botocore.exceptions import ClientError

config = boto3.client('config')

try:
    response = config.put_config_rule(
        ConfigRule={
            'ConfigRuleName': 'S3BucketRule',
            'Description': 'S3 Public Read Prohibited Bucket Rule',
            'Scope': {
                'ComplianceResourceTypes': [
                    'AWS::S3::Bucket',
                ],
            },
            'Source': {
                'Owner': 'AWS',
                'SourceIdentifier': 'S3_BUCKET_PUBLIC_READ_PROHIBITED',
            },
            'InputParameters': '{}',
            'ConfigRuleState': 'ACTIVE'
        }
    )
    print('\n\rResponse: ' + str(response) + '\n\r')
except ClientError as e:
    print(e)