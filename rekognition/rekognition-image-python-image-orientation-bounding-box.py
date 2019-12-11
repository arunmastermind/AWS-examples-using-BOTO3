import boto3
from PIL import Image       # To install package: pip install Pillow


def ShowBoundingBoxPositions(imageHeight, imageWidth, box, rotation):
    """Calculate the bounding box surrounding an identified face.

    The calculation takes the image rotation into account.

    :param imageHeight: Height of entire image in pixels
    :param imageWidth: Width of entire image in pixels
    :param box: Dictionary containing bounding box data points
    :param rotation: Image orientation determined by Rekognition
    """

    # Calculate left and top points taking image rotation into account
    left = 0
    top = 0
    if rotation == 'ROTATE_0':
        left = imageWidth * box['Left']
        top = imageHeight * box['Top']
    
    if rotation == 'ROTATE_90':
        left = imageHeight * (1 - (box['Top'] + box['Height']))
        top = imageWidth * box['Left']

    if rotation == 'ROTATE_180':
        left = imageWidth - (imageWidth * (box['Left'] + box['Width']))
        top = imageHeight * (1 - (box['Top'] + box['Height']))

    if rotation == 'ROTATE_270':
        left = imageHeight * box['Top']
        top = imageWidth * (1- box['Left'] - box['Width'] )

    print('Bounding box of face:')
    print(f'  Left: {round(left)}, Top: {round(top)}, '
          f'Width: {round(imageWidth * box["Width"])}, '
          f'Height: {round(imageHeight * box["Height"])}')


if __name__ == "__main__":
    """Exercise the Rekognition recognize_celebrities() method and 
    ShowBoundingBoxPositions()"""

    # Set the photo variable to the image filename to process
    photo = 'CELEBRITY_PHOTO.JPG'

    # Extract the image width, height, and EXIF data
    try:
        with Image.open(photo) as image:
            width, height = image.size
            exif = None
            if 'exif' in image.info:
                exif = image.info['exif']
    except IOError as e:
        print(e)
        exit(1)
    print(f'File name: {photo}')
    print(f'Image width, height: {width}, {height}')

    # Read the entire image into memory
    try:
        with open(photo, 'rb') as f:
            image_binary = f.read()
    except IOError as e:
        print(e)
        exit(2)

    # Detect the celebrities in the photo
    client = boto3.client('rekognition', region_name='us-east-1')
    response = client.recognize_celebrities(Image={'Bytes': image_binary})

    if 'OrientationCorrection' in response:
        print(f'Image orientation: {response["OrientationCorrection"]}')
    else:
        print('No estimated orientation. Check the image\'s Exif metadata.')

    # List the identified celebrities
    print('Detected celebrities...')
    celebrities = response['CelebrityFaces']
    if not celebrities:
        print('No celebrities detected')
    else:
        for celebrity in celebrities:
            print(f'\nName: {celebrity["Name"]}')
            print(f'Match confidence: {celebrity["MatchConfidence"]}')

            # List the bounding box that surrounds the face
            if 'OrientationCorrection' in response:
                ShowBoundingBoxPositions(height, width,
                                         celebrity['Face']['BoundingBox'],
                                         response['OrientationCorrection'])