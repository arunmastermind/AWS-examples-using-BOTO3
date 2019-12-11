import boto3

# your support case id
case_id='case-123456789012-muen-2019-e23abb614ab25793'

# file name to attach to support case
file_name="test.jpg"

# body of communication to add to case
communication_body = 'add attachment test'

support = boto3.client('support', region_name = 'us-east-1')

with open(file_name, mode='rb') as file:
    file_data = file.read()

attachment1 = { 'fileName' : file_name ,'data' : file_data }

attachment_set = support.add_attachments_to_set(
    attachments=[
        attachment1,
    ]
) 

add_communication_response = support.add_communication_to_case(
    caseId = case_id,
    communicationBody = communication_body,
    attachmentSetId = attachment_set['attachmentSetId'],
)

if add_communication_response['result']:
    print('Communication with attachment successfully added.')