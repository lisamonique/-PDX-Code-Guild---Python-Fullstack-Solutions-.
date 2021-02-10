print("Lab: Mini Capstone")


import re
import requests
import json


query = input("What Plant would you like to know about? ")

url = f"https://trefle.io/api/v1/plants/search?token=1qrtaYh3cqEUd5b_WeKFpum087I2sWiB0vd2ewOCceM&q={query}&order[year]=asc"

# API endpoint requires an API key be included in a request header
headers = {'Authorization': 'Token token="1qrtaYh3cqEUd5b_WeKFpum087I2sWiB0vd2ewOCceM"'}

# parse the JSON in the response into a python dictionary
response = requests.get(url, headers=headers)

plant_data = json.loads(response.text)

for item in plant_data['data']:
    print("----------Basic Plant Details------")
    print(f'Commom Name: {item["common_name"]}')
    print(f'Scientific Name: {item["scientific_name"]}')
    print(f'Year: {item["year"]}')
    print(f'Rank: {item["rank"]}')
    print("-----------------------------------")

