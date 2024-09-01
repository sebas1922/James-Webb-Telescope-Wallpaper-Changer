import requests
import json
import argparse
import random
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os 

api_key = os.getenv("FLICKR_API_KEY")

ALBUM_IDS = [{"year": 2024, "Id": "72177720313923911"}, {"year":2023, "Id":"72177720305127361"}, {"year":2022, "Id": "72177720305127361"}]
url = "https://www.flickr.com/photos/nasawebbtelescope/albums/"+random.choice(ALBUM_IDS)["Id"]

payload = {}
headers = {}


response = requests.get(url, headers=headers, data=payload)

print(response)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.find("div", {"class": "view album-page-view flickr-view-root-view"}))


"""
First get the id of each image from the response and put into a list
"""

#print(json.dumps(photo_data, indent=4))

image_id = []
for image in photo_data:
    image_id.append(image["id"])   


"""
Next we need to get the url of each image from the id and through there we can download the image itself
"""


for Id in image_id:
    url = f"https://www.flickr.com/photos/nasawebbtelescope/"+Id
    print(requests.get(url).content)
    

 
