import boto3


# Create CloudFront client
cf = boto3.client('cloudfront')

# List distributions with the pagination interface
print("\nCloudFront Distributions:\n")
paginator = cf.get_paginator('list_distributions')
for distributionlist in paginator.paginate():
  if distributionlist['DistributionList']['Quantity'] > 0:
    for distribution in distributionlist['DistributionList']['Items']:
      #print(distribution)
      print("Domain: " + distribution['DomainName'])
      print("Distribution Id: " + distribution['Id'])
      print("Certificate Source: " + distribution['ViewerCertificate']['CertificateSource'])
      if (distribution['ViewerCertificate']['CertificateSource'] == "acm"):
        print("Certificate ARN: " + distribution['ViewerCertificate']['Certificate'])
      print("")
  else:    
    print("Error - No CloudFront Distributions Detected.")