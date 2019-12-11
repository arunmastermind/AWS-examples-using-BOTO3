import boto3
from botocore.exceptions import ClientError

config = boto3.client('config')

rule_to_describe = 'S3BucketRule'

try:
    response = config.describe_config_rules(
        ConfigRuleNames=[
            rule_to_describe,
        ]
    )
    print('\n\rResponse: ' + str(response))
except ClientError as e:
    print(e)