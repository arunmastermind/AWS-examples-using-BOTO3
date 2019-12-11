from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Movies')

title = "The Big New Movie"
year = 2015

response = table.get_item(
    Key={
        'year': year,
        'title': title
    })

item = response['Item']

item['info']['rating'] = decimal.Decimal(5.5)
item['info']['plot'] = "Everything happens all at once."
item['info']['actors'] = ["Larry", "Moe", "Curly"]

table.put_item(Item=item)

response = table.get_item(
    Key={
        'year': year,
        'title': title
    })
item = response['Item']

print(json.dumps(item, indent=4, cls=DecimalEncoder))