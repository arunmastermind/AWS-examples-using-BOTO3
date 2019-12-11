import json
import boto3
import random

kinesis = boto3.client('kinesis')
def getReferrer():
    data = {}
    data['REFERRER'] = 'http://www.amazon.com'
    return data

while True:
        data = json.dumps(getReferrer())
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")