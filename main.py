import requests
import json
import argparse
from random import choice
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import platform
import ctypes

def main():
    load_dotenv()

    PLATFORM = platform.system()
    print(PLATFORM)
    API_KEY = os.getenv("FLICKR_API_KEY")
    JWST_ALBUM = [{"year": 2024, "Id": "72177720313923911"}, {"year":2023, "Id":"72177720305127361"}, {"year":2022, "Id": "72177720305127361"}]
    URL = "https://flickr.com/services/rest/"

    payload = {"api_key": API_KEY}
    headers = {}

    user_id = (get_user_id(URL, payload))

    
    # get list of photos in one of the three JWST albums
    album_photos = requests.get(URL+"?method=flickr.photosets.getPhotos", headers=headers, params=payload | {"photoset_id": JWST_ALBUM[0]["Id"]})
    soup = BeautifulSoup(album_photos.text, "xml")
    
    #Get the id and name of a random photo from the album
    photos = soup.find_all("photo")
    photo = choice(photos)
    photo_info = {"name": photo.attrs["title"],"photo_id": choice(photo.parent()).attrs["id"]}

    #print(photo_info)["name"]

    #Request and save the original download link for the photo
    photo_download_links = requests.get(URL+"?method=flickr.photos.getSizes", headers=headers, params=payload | {"photo_id": photo_info["photo_id"]})
    soup = BeautifulSoup(photo_download_links.text, "xml").find("size", {"label": "Original"})
    file_download_link = soup.attrs["source"]
    
    main_dir = os.getcwd()

    #Download the image
    if("images" not in os.listdir(main_dir)):
        os.mkdir("images")
        print("Creating directory 'things'...")

    r = requests.get(file_download_link)
    file_path = f"{main_dir}/images/{photo_info["name"]}.jpg"
    with open(file_path, "wb") as f:
        f.write(r.content)

    print(f"Downloaded {photo_info["name"]}.jpg")

    #set the wallpaper depending on the operating system
    if (PLATFORM == "Windows"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file_path, 0)
    elif(PLATFORM == "Linux"):
        os.system(f"xdg-open {main_dir}/images/{photo_info['name']}.jpg")
    

   



def get_user_id(url, payload):
    """
    Function to get the user id from the flickr API.

    Args:
        url (str): The base url for the flickr API.
        payload (dict): The payload to send with the request.

    Returns:
        dict: The response from the API containing the user id.
    """
    r = requests.get(url+"?method=flickr.people.findByUsername", params= payload | {"username" : "James Webb Space Telescope"})
    soup = BeautifulSoup(r.text, "xml")
    return soup.find("user").parent()[0].attrs["nsid"]
    
    


if __name__ == "__main__":
    main()