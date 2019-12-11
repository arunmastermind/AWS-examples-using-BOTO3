import boto3

# Create an SNS client
sns = boto3.client('sns')

# Call SNS to list the first 100 subscriptions
response = sns.list_subscriptions()

# Get a list of subscriptions from the response
subscriptions = []
for subscription in response['Subscriptions']:
    subscriptions.append(subscription)

# Print out the subscriptions list
print("Subscription List: %s" % subscriptions)