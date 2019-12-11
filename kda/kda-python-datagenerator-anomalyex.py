import json
import boto3
import random

kinesis = boto3.client('kinesis')

# Generate normal blood pressure with a 0.995 probability
def getNormalBloodPressure():
    data = {}
    data['Systolic'] = random.randint(90, 120)
    data['Diastolic'] = random.randint(60, 80)
    data['BloodPressureLevel'] = 'NORMAL'
    return data
    
# Generate high blood pressure with probability 0.005
def getHighBloodPressure():
    data = {}
    data['Systolic'] = random.randint(130, 200)
    data['Diastolic'] = random.randint(90, 150)
    data['BloodPressureLevel'] = 'HIGH'
    return data
    
# Generate low blood pressure with probability 0.005
def getLowBloodPressure():
    data = {}
    data['Systolic'] = random.randint(50, 80)
    data['Diastolic'] = random.randint(30, 50)
    data['BloodPressureLevel'] = 'LOW'
    return data

while True:
    rnd = random.random()
    if (rnd < 0.005):
        data = json.dumps(getLowBloodPressure())
        print(data)
        kinesis.put_record(
                StreamName="BloodPressureExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")
    elif (rnd > 0.995):
        data = json.dumps(getHighBloodPressure())
        print(data)
        kinesis.put_record(
                StreamName="BloodPressureExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")
    else:
        data = json.dumps(getNormalBloodPressure())
        print(data)
        kinesis.put_record(
                StreamName="BloodPressureExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")