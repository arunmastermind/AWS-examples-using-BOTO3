import boto3


# Set these values before running the program
input_s3_url = 's3://INPUT_BUCKET'
input_doc_format = 'ONE_DOC_PER_LINE'
output_s3_url = 's3://OUTPUT_BUCKET'
data_access_role_arn = 'arn:aws:iam::ACCOUNT_ID:role/DATA_ACCESS_ROLE'
classifier_arn = 'arn:aws:comprehend:region:ACCOUNT_ID:document-classifier/CLASSIFIER_NAME'

# Set up job configuration
input_data_config = {'S3Uri': input_s3_url, 'InputFormat': input_doc_format}
output_data_config = {'S3Uri': output_s3_url}

# Start classification job
client = boto3.client('comprehend')
start_response = client.start_document_classification_job(
    InputDataConfig=input_s3_url,
    OutputDataConfig=output_s3_url,
    DataAccessRoleArn=data_access_role_arn,
    DocumentClassifierArn=classifier_arn)
job_id = start_response['JobId']
print(f'Started Document Classification Job ID: {job_id}')

# Check the status of the job
describe_response = client.describe_document_classification_job(JobId=job_id)
job_status = describe_response['DocumentClassificationJobProperties']['JobStatus']
print(f'Status: {job_status}')
if job_status == 'FAILED':
    print(f'Reason: {describe_response["DocumentClassificationJobProperties"]["Message"]}')

# List recent classification jobs
list_response = client.list_document_classification_jobs()
for job in list_response['DocumentClassificationJobPropertiesList']:
    print(f'Job ID: {job["JobId"]}, Status: {job["JobStatus"]}')
