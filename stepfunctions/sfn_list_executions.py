import boto3

# The Amazon Resource Name (ARN) of the state machine to execute.
# Example - arn:aws:states:us-west-2:112233445566:stateMachine:HelloWorld-StateMachine
STATE_MACHINE_ARN = 'statemachineArn'

sfn = boto3.client('stepfunctions')

response = sfn.list_executions(
    stateMachineArn = STATE_MACHINE_ARN
)

print(response)