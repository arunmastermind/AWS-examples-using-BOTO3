import boto3

# Create SES client
ses = boto3.client('ses')

# Create receipt filter
response = ses.create_receipt_filter(
  Filter = {
    'NAME'     : 'NAME',
    'IpFilter' : {
      'Cidr'   : 'IP_ADDRESS_OR_RANGE',
      'Policy' : 'Allow' | 'Block'
    }
  }
)

print(response)