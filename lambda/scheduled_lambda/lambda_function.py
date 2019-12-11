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

    # Log that the function was invoked and the values received in the event
    # argument
    logger.info('Scheduled Lambda function was invoked')
    logger.info(f'Request event: {event}')

    # Construct response
    response = {'statusCode': 200}
    return response
