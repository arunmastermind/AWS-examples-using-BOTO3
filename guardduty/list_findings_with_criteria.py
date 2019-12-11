import boto3

# Create GuardDuty client
gd = boto3.client('guardduty')

# Get the GuardDuty Detector for the current AWS Region
detector = gd.list_detectors()
detectorid = detector['DetectorIds'][0]

# Finding Criteria for severity in this example must be greater than or
# equal to the value specified in Gte
fc = {'Criterion': {'severity': {'Gte': 4}}}

# Finding Criteria for type in this example can be equal to either of the
# two values specified in Eq
fc = {'Criterion': {'type': {'Eq': ['Recon:EC2/PortProbeUnprotectedPort',
                                    'Recon:EC2/Portscan']}}}

findings = gd.list_findings(DetectorId=detectorid,FindingCriteria=fc)

# Print out each finding
for finding in findings['FindingIds']:
    find_detail = gd.get_findings(DetectorId=detectorid, FindingIds=[finding])
    print(f'{find_detail}\n')