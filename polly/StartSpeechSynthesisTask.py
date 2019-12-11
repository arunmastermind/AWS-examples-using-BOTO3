import boto3

# Start synthesizing some text and save it as an MP3 audio file in an S3 file
polly_client = boto3.client('polly')
response = polly_client.start_speech_synthesis_task(
    VoiceId='Joanna',
    OutputS3BucketName='synth-books-buckets',
    OutputS3KeyPrefix='key',
    OutputFormat='mp3',
    Text='This is sample text to synthesize.')

# Output the task ID
taskId = response['SynthesisTask']['TaskId']
print(f'Task id is {taskId}')

# Retrieve and output the current status of the task
task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)
print(f'Status: {task_status}')