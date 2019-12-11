import boto3

# Assign this variable the SQS queue URL before running the program
queue_url = 'SQS_QUEUE_URL'

# Receive message from SQS queue
sqs = boto3.client('sqs')
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp',
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All',
    ],
)

# Extract response info
message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

# Change visibility timeout of message from queue
sqs.change_message_visibility(QueueUrl=queue_url,
                              ReceiptHandle=receipt_handle,
                              VisibilityTimeout=3600)
print(f'Received and changed visibility timeout of message: {message}')
