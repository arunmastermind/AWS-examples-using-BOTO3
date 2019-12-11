import greengrasssdk
import json

TOPIC_REQUEST = 'modbus/adapter/request'

# Creating a greengrass core sdk client
iot_client = greengrasssdk.client('iot-data')

def create_read_coils_request():
	request = {
		"request": {
			"operation": "ReadCoilsRequest",
			"device": 1,
			"address": 0x01,
			"count": 1
		},
		"id": "TestRequest"
	}
	return request

def publish_basic_request():
	iot_client.publish(payload=json.dumps(create_read_coils_request()), topic=TOPIC_REQUEST)

publish_basic_request()

def function_handler(event, context):
	return