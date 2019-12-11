import boto3
from botocore.exceptions import ClientError

region = "us-east-1"

# The phone number or short code to send the message from. The phone number
# or short code that you specify has to be associated with your Amazon Pinpoint
# account. For best results, specify long codes in E.164 format.
originationNumber = "+12065550199"

# The recipient's phone number.  For best results, you should specify the
# phone number in E.164 format.
destinationNumber = "+14255550142"

# The content of the SMS message.
message = ("This is a sample message sent from Amazon Pinpoint by using the "
           "AWS SDK for Python (Boto 3).")

# The Amazon Pinpoint project/application ID to use when you send this message.
# Make sure that the SMS channel is enabled for the project or application
# that you choose.
applicationId = "ce796be37f32f178af652b26eexample"

# The type of SMS message that you want to send. If you plan to send
# time-sensitive content, specify TRANSACTIONAL. If you plan to send
# marketing-related content, specify PROMOTIONAL.
messageType = "TRANSACTIONAL"

# The registered keyword associated with the originating short code.
registeredKeyword = "myKeyword"

# The sender ID to use when sending the message. Support for sender ID
# varies by country or region.
senderId = "MySenderID"

# Create a new client and specify a region.
client = boto3.client('pinpoint',region_name=region)
try:
    response = client.send_messages(
        ApplicationId=applicationId,
        MessageRequest={
            'Addresses': {
                destinationNumber: {
                    'ChannelType': 'SMS'
                }
            },
            'MessageConfiguration': {
                'SMSMessage': {
                    'Body': message,
                    'Keyword': registeredKeyword,
                    'MessageType': messageType,
                    'OriginationNumber': originationNumber,
                    'SenderId': senderId
                }
            }
        }
    )

except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Message sent! Message ID: "
            + response['MessageResponse']['Result'][destinationNumber]['MessageId'])