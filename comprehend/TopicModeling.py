import boto3

# Set these values before running the program
input_s3_url = 's3://INPUT_BUCKET'
input_doc_format = 'ONE_DOC_PER_FILE'
output_s3_url = 's3://OUTPUT_BUCKET'
data_access_role_arn = 'arn:aws:iam::ACCOUNT_ID:role/DATA_ACCESS_ROLE'
number_of_topics = 10   # Optional argument

# Set up job configuration
input_data_config = {'S3Uri': input_s3_url, 'InputFormat': input_doc_format}
output_data_config = {'S3Uri': output_s3_url}

# Begin a job to detect the topics in the document collection
comprehend = boto3.client('comprehend')
start_result = comprehend.start_topics_detection_job(
    InputDataConfig=input_data_config,
    OutputDataConfig=output_data_config,
    DataAccessRoleArn=data_access_role_arn,
    NumberOfTopics=number_of_topics)
job_id = start_result['JobId']
print(f'Started Topic Detection Job: {job_id}')

# Retrieve information about the job
describe_result = comprehend.describe_topics_detection_job(JobId=job_id)
job_status = describe_result['TopicsDetectionJobProperties']['JobStatus']
print(f'Job Status: {job_status}')
if job_status == 'FAILED':
    print(f'Reason: {describe_result["TopicsDetectionJobProperties"]["Message"]}')

# List all topic-detection jobs
list_result = comprehend.list_topics_detection_jobs()
for job in list_result['TopicsDetectionJobPropertiesList']:
    print(f'Job ID: {job["JobId"]}, Status: {job["JobStatus"]}')

