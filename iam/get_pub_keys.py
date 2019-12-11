import boto3

user_name = 'your-name'

# Create IAM client
iam = boto3.client('iam')

ssh_public_keys_response = iam.list_ssh_public_keys(
    UserName = user_name,
    MaxItems = 100,
)

# Get SSH public key
for ssh_public_key in ssh_public_keys_response['SSHPublicKeys']:
    ssh_public_key = ssh_public_key['SSHPublicKeyId']
    ssh_public_key_response = iam.get_ssh_public_key(
        UserName = user_name,
        SSHPublicKeyId = ssh_public_key,
        Encoding = 'SSH',
    )
    print(ssh_public_key_response['SSHPublicKey']['SSHPublicKeyBody'])