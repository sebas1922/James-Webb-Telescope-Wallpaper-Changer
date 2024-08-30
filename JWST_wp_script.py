import requests
from bs4 import BeautifulSoup
import json
import requests



url = "https://api.flickr.com/services/rest?per_page=25&page=1&user_id=50785054%40N03&sort=use_pref&method=flickr.people.getPhotos&api_key=33bccb4d64c438d98864f72434cfc044&format=json&nojsoncallback=1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload).json()


"""
First get the id of each image from the response and put into a list
"""
photo_data = response["photos"]["photo"]
print(json.dumps(photo_data, indent=4))

image_id = []

for image in photo_data:
    image_id.append(image["id"])   


"""
Next we need to get the url of each image from the id and through there we can download the image itself
"""


for image in image_id:
    url = f"https://www.flickr.com/photos/nasawebbtelescope/"
    print(url)


 
