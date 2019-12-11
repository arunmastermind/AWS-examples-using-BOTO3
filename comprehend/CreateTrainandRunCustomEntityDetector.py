import boto3
import time
import uuid

comprehend = boto3.client('comprehend')
response = comprehend.create_entity_recognizer(
    RecognizerName="Recognizer-Name-Goes-Here-{}".format(str(uuid.uuid4())),
    LanguageCode="en",
    DataAccessRoleArn="Role ARN",
    InputDataConfig={
        "EntityTypes": [
            {
                "Type": "ENTITY_TYPE"
            }
        ],
        "Documents": {
            "S3Uri": "s3://Bucket Name/Bucket Path/documents"
        },
        "Annotations": {
            "S3Uri": "s3://Bucket Name/Bucket Path/annotations"
        }
    }
)
recognizer_arn = response['EntityRecognizerArn']

response = comprehend.list_entity_recognizers()

trained = False
while not trained:

    response = comprehend.describe_entity_recognizer(
        EntityRecognizerArn=recognizer_arn
    )
    status = response['EntityRecognizerProperties']['Status']
    if status == 'IN_ERROR':
        exit(1)
    elif status == 'TRAINED':
        trained = True
        continue

    time.sleep(10)
    
    response = comprehend.start_entities_detection_job(
        EntityRecognizerArn=recognizer_arn,
        JobName='Detection-Job-Name-{}'.format(str(uuid.uuid4())),
        LanguageCode='en',
        DataAccessRoleArn='ROLE_ARN',
        InputDataConfig={
            'InputFormat': 'ONE_DOC_PER_LINE',
            'S3Uri': 's3://BUCKET_NAME/BUCKET_PATH/documents'
        },
        OutputDataConfig={
            'S3Uri': 's3://BUCKET_NAME/BUCKET_PATH/output'
        })