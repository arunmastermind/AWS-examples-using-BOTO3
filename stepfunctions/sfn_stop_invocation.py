import boto3

# The Amazon Resource Name (ARN) of the execution to stop.
# Example - arn:aws:states:us-west-2:112233445566:execution:HelloWorld-StateMachine
EXECUTION_ARN = 'executionARN'


sfn = boto3.client('stepfunctions')

response = sfn.stop_execution(
    executionArn=EXECUTION_ARN,
)

#display the arn that identifies the execution
print(response)