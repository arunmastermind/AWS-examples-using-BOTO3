import greengrasssdk
import platform
import time
import json

client = greengrasssdk.client('iot-data')

my_platform = platform.platform()

my_counter = 0

def function_handler(event, context):
    global my_counter
    my_counter = my_counter + 1
    if not my_platform:
        client.publish(
            topic='hello/world/counter',
            payload=json.dumps({'message': 'Hello world! Sent from Greengrass Core.  Invocation Count: {}'.format(my_counter)})
        )
    else:
        client.publish(
            topic='hello/world/counter',
            payload=json.dumps({'message': 'Hello world! Sent from Greengrass Core running on platform: {}.  Invocation Count: {}'
                                .format(my_platform, my_counter)})
        )
    time.sleep(20)
    return