import time
import os
import DeepLens_Kinesis_Video as dkv
from botocore.session import Session
import greengrasssdk

def greengrass_hello_world_run():
    # Create the green grass client so that we can send messages to IoT console
    client = greengrasssdk.client('iot-data')
    iot_topic = '$aws/things/{}/infer'.format(os.environ['AWS_IOT_THING_NAME'])

    # Stream configuration, name and retention
    # Note that the name will appear as deeplens-myStream
    stream_name = 'myStream'
    retention = 2 #hours

    # Amount of time to stream
    wait_time = 60 * 60 * 5 #seconds

    # Use the boto session API to grab credentials
    session = Session()
    creds = session.get_credentials()

    # Create producer and stream.
    producer = dkv.createProducer(creds.access_key, creds.secret_key, creds.token, "us-east-1")
    client.publish(topic=iot_topic, payload="Producer created")
    kvs_stream = producer.createStream(stream_name, retention)
    client.publish(topic=iot_topic, payload="Stream {} created".format(stream_name))

    # Start putting data into the KVS stream
    kvs_stream.start()
    client.publish(topic=iot_topic, payload="Stream started")
    time.sleep(wait_time)
    # Stop putting data into the KVS stream
    kvs_stream.stop()
    client.publish(topic=iot_topic, payload="Stream stopped")

# Execute the function above
greengrass_hello_world_run()