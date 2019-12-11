import json
import boto3
import random

kinesis = boto3.client('kinesis')
def getReferrer():
    data = {}
    data['LOGENTRY'] = '203.0.113.24 - - [25/Mar/2018:15:25:37 -0700] "GET /index.php HTTP/1.1" 200 125 "-" "Mozilla/5.0 [en] Gecko/20100101 Firefox/52.0"'
    return data

while True:
        data = json.dumps(getReferrer())
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")