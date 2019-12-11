import boto3

# Synthesize the sample text, saving it in an MP3 audio file
polly_client = boto3.client('polly')
response = polly_client.synthesize_speech(VoiceId='Joanna',
                                          OutputFormat='mp3',
                                          Text='This is sample text to synthesize.')
with open('speech.mp3', 'w') as file:
    file.write(response['AudioStream'].read())