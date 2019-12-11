import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Get URL for SQS queue
response = sqs.get_queue_url(QueueName='SQS_QUEUE_NAME')

print(response['QueueUrl'])