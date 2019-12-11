import greengrasssdk
 
# Create SDK clients.
secrets_client = greengrasssdk.client('secretsmanager')
message_client = greengrasssdk.client('iot-data')
message = ''

# This handler is called when the function is invoked.
# It uses the 'secretsmanager' client to get the value of the test secret using the secret name.
# The test secret is a text type, so the SDK returns a string. 
# For binary secret values, the SDK returns a base64-encoded string.
def function_handler(event, context):
    response = secrets_client.get_secret_value(SecretId='greengrass-TestSecret')
    secret_value = response.get('SecretString')
    if secret_value is None:
        message = 'Failed to retrieve secret.'
    else:
        message = 'Success! Retrieved secret.'
    
    message_client.publish(topic='secrets/output', payload=message)
    print('published: ' + message)