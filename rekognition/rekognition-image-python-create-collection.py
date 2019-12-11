import boto3

if __name__ == "__main__":

    # Replace collectionID with the name of the collection that you want to create.
    maxResults = 2
    collectionId = 'MyCollection'

    # Create a collection
    print('Creating collection:' + collectionId)

    client=boto3.client('rekognition')
    response = client.create_collection(CollectionId=collectionId)

    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')