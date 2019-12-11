import boto3

if __name__ == "__main__":

    # Change collectionID to the collection that contains the face.
    # Change "xxxxxx..." to the ID of the face that you want to delete.

    collectionId='MyCollection'
    faces=[]
    faces.append("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

    client=boto3.client('rekognition')

    response=client.delete_faces(CollectionId=collectionId,
                               FaceIds=faces)
    
    print(str(len(response['DeletedFaces'])) + ' faces deleted:') 							
    for faceId in response['DeletedFaces']:
         print (faceId)