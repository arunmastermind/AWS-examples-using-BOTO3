import json

import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'SOURCE_QUEUE_URL'
dead_letter_queue_arn = 'DEAD_LETTER_QUEUE_ARN'

redrive_policy = {
    'deadLetterTargetArn': dead_letter_queue_arn,
    'maxReceiveCount': '10'
}


# Configure queue to send messages to dead letter queue
sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'RedrivePolicy': json.dumps(redrive_policy)
    }
)