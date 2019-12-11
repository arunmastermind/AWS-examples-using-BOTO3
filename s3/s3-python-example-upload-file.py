import boto3

# Create an S3 client
S3 = boto3.client('s3')

SOURCE_FILENAME = 'filename'
BUCKET_NAME = 'bucket-name'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
S3.upload_file(SOURCE_FILENAME, BUCKET_NAME, SOURCE_FILENAME)
