import json
import logging
import os
import boto3
from botocore.exceptions import ClientError

# Set up logging
logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """Example WebSocket $connect Lambda function

    :param event: Dict (usually) of parameters passed to the function
    :param context: LambdaContext object of runtime data
    :return: Dict of key:value pairs
    """

    # Log the values received in the event and context arguments
    logger.info('$connect event: ' + json.dumps(event, indent=2))
    logger.info(f'$connect event["requestContext"]["connectionId"]: {event["requestContext"]["connectionId"]}')

    # Retrieve the name of the DynamoDB table to store connection IDs
    table_name = os.environ['TableName']

    # Was a user name specified in a query parameter?
    user_name = 'Anon'
    if 'queryStringParameters' in event:
        if 'name' in event['queryStringParameters']:
            user_name = event['queryStringParameters']['name']

    # Store the connection ID and user name in the table
    item = {'connectionId': {'S': event['requestContext']['connectionId']},
            'userName': {'S': user_name}}
    dynamodb_client = boto3.client('dynamodb')
    try:
        dynamodb_client.put_item(TableName=table_name, Item=item)
    except ClientError as e:
        logger.error(e)
        raise ConnectionAbortedError(e)

    # Construct response
    response = {'statusCode': 200}
    return response
