import boto3

if __name__ == "__main__":

    # Change the values of photo and bucket to your values.
    photo='moderate.png'
    bucket='bucket'
    
    client=boto3.client('rekognition')

    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    print('Detected labels for ' + photo)    
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])