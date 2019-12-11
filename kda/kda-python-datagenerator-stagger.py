import json
import boto3
import random
import datetime
import time

kinesis = boto3.client('kinesis')
def getData():
    data = {}
    now = datetime.datetime.utcnow() - datetime.timedelta(seconds=10)
    str_now = now.isoformat()
    data['EVENT_TIME'] = str_now
    data['TICKER'] = random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV'])
    return data

while True:
    data = json.dumps(getData())
    # Send six records, ten seconds apart, with the same event time and ticker
    for x in range(0, 6):
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")
        time.sleep(10)