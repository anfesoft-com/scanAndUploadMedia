import requests
from pathlib import Path
url = "https://upload.twitter.com/1.1/media/upload.json"
imagedirectory = 'PATH_TO_IMAGE_FOLDER_HERE'

def  saveImageid(imageid):
	f = open("uploaded.txt", "a")
	f.write(imageid+'\n')


def pushup(theimage):
	payload={}
	files=[
	('media',('creator.jpeg',open(theimage,'rb'),'image/jpeg'))
	]
	headers = {
	'Authorization': 'OAuth oauth_consumer_key="YOUR_CONSUMER_KEY_HERE",oauth_token="YOUR_TOKEN_HERE",oauth_signature_method="HMAC-SHA1",oauth_timestamp="TIMESTAMPHERE",oauth_nonce="YOURNOUNCE",oauth_version="1.0",oauth_signature="YOUR_SIGNATURE"',
	'Cookie': 'guest_id=v1%3A164931910107415512; lang=en'
	}
	response = requests.request("POST", url, headers=headers, data=payload, files=files)
	print(response.text)

for elem in Path(imagedirectory).rglob('*.jpeg'):
    pushup(elem)
