import boto3

# The name of the state machine
SF_NAME = 'HelloWorld-StateMachine'

# The Amazon States Language definition of the state machine
HELLO_WORLD_SF_DEF = '{"StartAt": "HelloWorld", "States": ' \
                     '{"HelloWorld": {"Type": "Pass", "Result": "Hello World!", "End": true}}}'

# Arn of the IAM role to use for this state machine
# Replace the value with a valid RoleArn
ROLE_ARN = 'roleArn'

sfn = boto3.client('stepfunctions')

response = sfn.create_state_machine(
    name=SF_NAME,
    definition=HELLO_WORLD_SF_DEF,
    roleArn=ROLE_ARN
)

# print the statemachine Arn
print(response.get('stateMachineArn'))