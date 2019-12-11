import boto3

if __name__ == "__main__":

    # Change the value of id to an ID value returned by RecognizeCelebrities or GetCelebrityRecognition

    id="nnnnnnnn"

    client=boto3.client('rekognition')

    #Display celebrity info
    print('Getting celebrity info for celebrity: ' + id)
    response=client.get_celebrity_info(Id=id)

    print (response['Name'])  
    print ('Further information (if available):')
    for url in response['Urls']:
        print (url)