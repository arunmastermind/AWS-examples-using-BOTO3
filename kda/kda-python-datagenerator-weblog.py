import json
import boto3
import random

kinesis = boto3.client('kinesis')
def getLog():
    data = {}
    data['log'] = '192.168.254.30 - John [24/May/2004:22:01:02 -0700] "GET /icons/apache_pb.gif HTTP/1.1" 304 0'
    return data

while True:
        data = json.dumps(getLog())
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")