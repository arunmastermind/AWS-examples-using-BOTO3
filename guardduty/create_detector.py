import boto3

def create_detector(client):
    client.create_detector();

region='us-east-1'

# Create GuardDuty client
gd = boto3.client(
    service_name='guardduty',
    region_name=region
    )

#Get the GuardDuty Detector for the current AWS Region
detector=gd.list_detectors()
if len(detector['DetectorIds']) > 0:
    detector_id = detector['DetectorIds'][0]
    print('Detector exists in Region ' + region + ' Detector Id: ' + detector_id)
else:
    print('GuardDuty Detector does not exist in Region ' + region)
    print('Creating Detector in ' + region + ' ...')
    create_detector(gd)