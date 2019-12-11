import boto3

# The Amazon Resource Name (ARN) of the state machine to execute.
# Example - arn:aws:states:us-west-2:112233445566:stateMachine:HelloWorld-StateMachine
STATE_MACHINE_ARN = 'statemachineArn'

#The name of the execution
EXECUTION_NAME = 'HelloWorld-StateMachine-Exec3'

#The string that contains the JSON input data for the execution
INPUT = "{}"

sfn = boto3.client('stepfunctions')

response = sfn.start_execution(
    stateMachineArn=STATE_MACHINE_ARN,
    name=EXECUTION_NAME,
    input=INPUT
)

#display the arn that identifies the execution
print(response.get('executionArn'))