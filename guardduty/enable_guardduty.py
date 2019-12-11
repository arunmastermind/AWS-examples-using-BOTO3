import boto3

regions_to_enable='us-east-1 us-west-2'

def create_detector(client):
    client.create_detector();

def enable_detector(client, detector):
    client.update_detector(
        DetectorId=detector,
        Enable=True
    )

try:
    for region in regions_to_enable.split():
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
        create_detector(client=gd)
    
    detector=gd.list_detectors()
    if len(detector['DetectorIds']) > 0:
        detector_id = detector['DetectorIds'][0]
        detector_details = gd.get_detector(DetectorId=detector_id)
        detector_status = detector_details['Status']
        print('Detector ID ' + detector_id + ' in Region ' + region + ' is ' + detector_status)
        if detector_status == 'DISABLED':
            print('Enabling Detector ' + detector_id + ' in ' + region + ' ...')
            enable_detector(client=gd,detector=detector_id)
    else:
        print('GuardDuty Detector does not exist in Region ' + region)
except Exception as e:
    print(e)