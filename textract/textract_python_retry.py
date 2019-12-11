import boto3
from botocore.client import Config


def process_multiple_documents(bucket, documents):
    
    config = Config(retries = dict(max_attempts = 5))
 
    # Amazon Textract client
    textract = boto3.client('textract', config=config)
 
    for documentName in documents:
 
        print("\nProcessing: {}\n==========================================".format(documentName))
 
        # Call Amazon Textract
        response = textract.detect_document_text(
            Document={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': documentName
                }
            })
 
        # Print detected text
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                print ('\033[94m' +  item["Text"] + '\033[0m')


def main():
    bucket = ""
    documents = ["document-image-1.png",
    "document-image-2.png", "document-image-3.png",
    "document-image-4.png", "document-image-5.png" ]
    process_multiple_documents(bucket, documents)



if __name__ == "__main__":
    main()