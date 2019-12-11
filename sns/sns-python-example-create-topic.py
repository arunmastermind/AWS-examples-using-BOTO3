import boto3

sns = boto3.client('sns')
response = sns.create_topic(Name='my-topic')

print(response)