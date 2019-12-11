import greengrasssdk
 
# Creating a greengrass core sdk client
client = greengrasssdk.client('secretsmanager')
 
# This handler is called when the function is invoked
# It uses the secretsmanager client to get the value of a specific secret version
def function_handler(event, context):
    response = client.get_secret_value(SecretId='greengrass-MySecret-abc', VersionStage='MyTargetLabel')
    raw_secret = response.get('SecretString')