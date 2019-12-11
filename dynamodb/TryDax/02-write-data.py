import os
import boto3

table_name = 'TryDaxTable'
some_data = 'X' * 1000
pk_max = 10
sk_max = 10

region = os.environ.get('AWS_DEFAULT_REGION', 'us-west-2')
dynamodb = boto3.client('dynamodb', region_name=region)
for ipk in range(1, pk_max+1):
    for isk in range(1, sk_max+1):
        params = {
            'TableName': table_name,
            'Item': {
                'pk': {'N': str(ipk)},
                'sk': {'N': str(isk)},
                'someData': {'S': some_data}
            }
        }

        dynamodb.put_item(**params)
        print(f'PutItem ({ipk}, {isk}) succeeded')