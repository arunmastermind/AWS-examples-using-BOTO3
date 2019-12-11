import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to delete the website policy for the given bucket
s3.delete_bucket_website(Bucket='BUCKET_NAME')