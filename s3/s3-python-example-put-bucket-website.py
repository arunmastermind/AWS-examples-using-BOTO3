import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create the configuration for the website
website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

# Set the new policy on the selected bucket
s3.put_bucket_website(
    Bucket='my-bucket',
    WebsiteConfiguration=website_configuration
)