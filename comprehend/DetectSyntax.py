import boto3
import json
 
comprehend = boto3.client(service_name='comprehend', region_name='region')
text = "It is raining today in Seattle"
 
print('Calling DetectSyntax')
print(json.dumps(comprehend.detect_syntax(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSyntax\n')