import boto3

# The Amazon Resource Name (ARN) of the state machine to execute.
# Example - arn:aws:states:us-west-2:112233445566:stateMachine:HelloWorld-StateMachine
STATE_MACHINE_ARN = 'statemachineArn'

# Updated States Language definition of the state machine
HELLO_WORLD_SF_DEF = '{"StartAt": "HelloWorld", "States": ' \
                     '{"HelloWorld": {"Type": "Pass", "Result": "Hello World!", "End": true}}}'

# Arn of the IAM role to use for this state machine
# Replace the value with a valid RoleArn
ROLE_ARN = 'roleArn'

sfn = boto3.client('stepfunctions')

response = sfn.update_state_machine(
    stateMachineArn=STATE_MACHINE_ARN,
    definition=HELLO_WORLD_SF_DEF,
    roleArn=ROLE_ARN
)

print(response)