import boto3


# Create CloudWatchEvents client
cloudwatch_events = boto3.client('events')

# Put target for rule
response = cloudwatch_events.put_targets(
    Rule='DEMO_EVENT',
    Targets=[
        {
            'Arn': 'LAMBDA_FUNCTION_ARN',
            'Id': 'myCloudWatchEventsTarget',
        }
    ]
)
print(response)