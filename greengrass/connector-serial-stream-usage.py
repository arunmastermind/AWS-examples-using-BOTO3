import greengrasssdk
import json

TOPIC_REQUEST = 'serial/CORE_THING_NAME/write/dev/serial1'

# Creating a greengrass core sdk client
iot_client = greengrasssdk.client('iot-data')

def create_serial_stream_request():
	request = {
		"data": "TEST",
		"type": "ascii",
		"id": "abc123"
	}
	return request

def publish_basic_request():
	iot_client.publish(payload=json.dumps(create_serial_stream_request()), topic=TOPIC_REQUEST)

publish_basic_request()

def function_handler(event, context):
	return