import boto3


# Create CloudWatchLogs client
cloudwatch_logs = boto3.client('logs')

# Create a subscription filter
cloudwatch_logs.put_subscription_filter(
    destinationArn='LAMBDA_FUNCTION_ARN',
    filterName='FILTER_NAME',
    filterPattern='ERROR',
    logGroupName='LOG_GROUP',
)