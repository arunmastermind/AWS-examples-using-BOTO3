import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to get bucket tagging
bucket_tagging = s3.get_bucket_tagging(Bucket='my-bucket')

# Get a list of all tags
tag_set = bucket_tagging['TagSet']

# Print out each tag
for tag in tag_set:    
    print(tag) 