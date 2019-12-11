import json
import boto3
import random

kinesis = boto3.client('kinesis')

# generate normal heart rate with probability .99
def getNormalHeartRate():
    data = {}
    data['heartRate'] = random.randint(60, 100)
    data['rateType'] = "NORMAL"
    return data
# generate high heart rate with probability .01 (very few)
def getHighHeartRate():
    data = {}
    data['heartRate'] = random.randint(150, 200)
    data['rateType'] = "HIGH"
    return data

while True:
    rnd = random.random()
    if (rnd < 0.01):
        data = json.dumps(getHighHeartRate())
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")
    else:
        data = json.dumps(getNormalHeartRate())
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")