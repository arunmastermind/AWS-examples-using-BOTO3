import greengrasssdk
 
# Creating a Greengrass Core SDK client
client = greengrasssdk.client('secretsmanager')
 
# This handler is called when the function is invoked
# It uses the secretsmanager client to get the value of a secret
def function_handler(event, context):
    response = client.get_secret_value(SecretId='greengrass-MySecret-abc')
    raw_secret = response.get('SecretString')