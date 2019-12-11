import boto3


# Create CloudFront client
cf = boto3.client('cloudfront')

# List distributions
print("\nCloudFront Distributions:\n")
distributions=cf.list_distributions()
if distributions['DistributionList']['Quantity'] > 0:
  for distribution in distributions['DistributionList']['Items']:
    print("Domain: " + distribution['DomainName'])
    print("Distribution Id: " + distribution['Id'])
    print("Certificate Source: " + distribution['ViewerCertificate']['CertificateSource'])
    if (distribution['ViewerCertificate']['CertificateSource'] == "acm"):
      print("Certificate: " + distribution['ViewerCertificate']['Certificate'])
    print("")
else:    
  print("Error - No CloudFront Distributions Detected.")