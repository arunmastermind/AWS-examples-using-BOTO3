import json
import boto3
from botocore.exceptions import ClientError

# Assign the ID of an existing cluster to the following variable
job_flow_id = 'CLUSTER_ID'

# Define a job flow step. Assign appropriate values as desired.
job_flow_step_01 = {
    'Name': 'Example EMRFS Sync Step',
    'ActionOnFailure': 'CONTINUE',
    'HadoopJarStep': {
        'Jar': 's3://elasticmapreduce/libs/script-runner/script-runner.jar',
        'Args': [
            '/home/hadoop/bin/emrfs',
            'sync',
            's3://elasticmapreduce/samples/cloudfront'
        ]
    }
}

# Add the step(s)
emr_client = boto3.client('emr')
try:
    response = emr_client.add_job_flow_steps(JobFlowId=job_flow_id,
                                             Steps=[json.dumps(job_flow_step_01)])
except ClientError as e:
    print(e.response['Error']['Message'])
    exit(1)

# Output the IDs of the added steps
print('Step IDs:')
for stepId in response['StepIds']:
    print(stepId)