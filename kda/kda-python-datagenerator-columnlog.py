import json
import boto3
import random

kinesis = boto3.client('kinesis')

def getHighHeartRate():
    data = {}
    data['Col_A'] = 'a'
    data['Col_B'] = 'b'
    data['Col_C'] = 'c'
    data['Col_E_Unstructured'] = 'x,y,z'
    return data

while True:
        data = json.dumps(getHighHeartRate())
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")