import boto3

# Create an SNS client
sns = boto3.client('sns')

# Call SNS to list the first 100 subscriptions for the specified topic
response = sns.list_subscriptions_by_topic(
    TopicArn='arn:aws:sns:region:0123456789:my-topic-arn'    
    )

# Get a list of subscriptions from the response
#subscriptions = [subscription for subscription in response['Subscriptions']]
subscriptions = []
for subscription in response['Subscriptions']:
    subscriptions.append(subscription)

# Print out the subscriptions list
print("Subscription List: %s" % subscriptions)