import boto3

# Create an IAM service resource
resource = boto3.resource('iam')

# Get an iterable of all users
users = resource.users.all()

# Print details for each user
for user in users:
    print("User {} created on {}".format(
        user.user_name,
        user.create_date
    ))