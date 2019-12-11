import logging
logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """Basic Lambda function template

    :param event: Dict (usually) of parameters passed to the function
    :param context: LambdaContext object of runtime data
    :return: Dict of key:value pairs
    """

    # Log the values received in the event argument
    logger.info(f'Request event: {event}')

    # Define default hard-coded return values
    response = {
        'uid': 'Example function ID',
        'return_val01': 'Return value #1',
        'return_val02': 'Return Value #2',
    }

    # Retrieve type of invocation (GET, PUT, etc.)
    if 'http_verb' in event:
        operation = event['http_verb'].upper()
        if operation == 'PUT':
            # Return the values passed to the function
            response = {
                'uid': event['functionID'],
                'return_val01': event['parameters']['parm01'],
                'return_val02': event['parameters']['parm02'],
            }

    logger.info(f'Response={response}')
    return response
