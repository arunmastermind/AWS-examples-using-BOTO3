import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to retrieve CORS configuration for selected bucket
result = s3.get_bucket_cors(Bucket='my-bucket')