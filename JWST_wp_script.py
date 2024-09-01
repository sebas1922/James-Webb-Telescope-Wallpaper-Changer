import requests
import json
import argparse
from random import choice
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os 

def main():
    load_dotenv()

    api_key = os.getenv("FLICKR_API_KEY")

    ALBUM_IDS = [{"year": 2024, "Id": "72177720313923911"}, {"year":2023, "Id":"72177720305127361"}, {"year":2022, "Id": "72177720305127361"}]

    url = "https://api.flickr.com/services/rest/"

    payload = {"api_key": api_key}
    headers = {}


    #response = requests.get(url+"method=flickr.photosets.getList", headers=headers, params=payload)

    print(get_user_id(url, payload))




def get_user_id(url, payload):
    r = requests.get(url+"method=flickr.people.findByUsername", 
        params= payload | {"username" : "Flickr"})
    return r.content


if __name__ == "__main__":
    main()