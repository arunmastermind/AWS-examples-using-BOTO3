from __future__ import print_function

import os
import amazondax
import botocore.session

region = os.environ.get('AWS_DEFAULT_REGION', 'us-west-2')

session = botocore.session.get_session()
dynamodb = session.create_client('dynamodb', region_name=region) # low-level client

table_name = "TryDaxTable"

params = {
    'TableName' : table_name
}

# Delete the table
dynamodb.delete_table(**params)

# Wait for the table to be deleted before exiting
print('Waiting for', table_name, '...')
waiter = dynamodb.get_waiter('table_not_exists')
waiter.wait(TableName=table_name)