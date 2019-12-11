import boto3

# Create an SNS client
sns = boto3.client('sns')

# Send a SMS message to the specified phone number
response = sns.publish(
    PhoneNumber='MyPhoneNumber',
    Message='Hello World!',    
)

# Print out the response
print(response)