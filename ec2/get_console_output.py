import boto3

import sys

def get_console_output(instance_id):
    """
    Using EC2 GetConsoleOutput API according
        https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetConsoleOutput.html
    """
    ec2 = boto3.resource('ec2')
    ec2_instance = ec2.Instance(instance_id)
    json_output = ec2_instance.console_output()

    return json_output.get('Output', '')

def main():
    if len(sys.argv) == 1:
        print("Usage: {0} <instance-id>".format(sys.argv[0]))
        sys.exit(1)

    instance_id = sys.argv[1]
    output = get_console_output(instance_id)
    print(output)

    return 0

if __name__ == '__main__':
    sys.exit(main())