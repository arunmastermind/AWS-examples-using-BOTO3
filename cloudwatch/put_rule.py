import boto3


# Create CloudWatchEvents client
cloudwatch_events = boto3.client('events')

# Put an event rule
response = cloudwatch_events.put_rule(
    Name='DEMO_EVENT',
    ScheduleExpression='rate(5 minutes)',
    State='ENABLED'
)
print(response['RuleArn'])