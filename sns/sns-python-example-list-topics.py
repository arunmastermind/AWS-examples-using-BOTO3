import boto3

# Create an SNS client
sns = boto3.client('sns')

# Call SNS to list topics
response = sns.list_topics()

# Get a list of all topic ARNs from the response
topics = [topic['TopicArn'] for topic in response['Topics']]

# Print out the topic list
print("Topic List: %s" % topics)