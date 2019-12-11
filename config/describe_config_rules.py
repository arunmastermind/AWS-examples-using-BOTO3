import boto3
from botocore.exceptions import ClientError

config = boto3.client('config')

try:
    response = config.describe_config_rules()
    for rule in response['ConfigRules']:
       print('\n\r' + str(rule))
except ClientError as e:
    print(e)