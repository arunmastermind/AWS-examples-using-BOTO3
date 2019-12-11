import boto3



# Create CloudWatchLogs client
cloudwatch_logs = boto3.client('logs')

# Delete a subscription filter
cloudwatch_logs.delete_subscription_filter(
    filterName='FILTER_NAME',
    logGroupName='LOG_GROUP',
)