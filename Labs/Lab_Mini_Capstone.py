print("Lab: Mini Capstone")


import re
import requests
import json
import time


query = input("What Plant would you like to know about? ")

url = f"https://trefle.io/api/v1/plants/search?token=1qrtaYh3cqEUd5b_WeKFpum087I2sWiB0vd2ewOCceM&q={query}&order[year]=asc"

# API endpoint requires an API key be included in a request header
headers = {'Authorization': 'Token token="1qrtaYh3cqEUd5b_WeKFpum087I2sWiB0vd2ewOCceM"'}

# parse the JSON in the response into a python dictionary
response = requests.get(url, headers=headers)

plant_data = json.loads(response.text)

time.sleep(0.5)

print(f"Make selection from Menu to learn more about {query}! ")

time.sleep(3)

def display_main_menu():
    print('-------- MENU --------')
    print('  1. Get Plant Name')
    print('  2. Get Plant Year')
    print('  3. Get Plant Rank')
    print('  4. Exit Search')
    print('----------------------')

def exit():
    option = int(input(" Press 4 to return to Main Menu : "))

    if option == 4:
        run()
    else:
        print(" Invalid Option")
        exit()

def get_plant_name():

    print('------ Plant Name ------')
    
    for item in plant_data['data']:
        print(f'The Commom Name is {item["common_name"]}')
        print(f'The Scientific Name is {item["scientific_name"]}')

    print('----- End of Page ------')
    exit()


def get_plant_year():

    print('--------- Plant Year --------')
    
    for item in plant_data['data']:
        print(f'The {item["common_name"]} was entered into the plant directory in Year: {item["year"]}')

    print('-------- End of Page --------')
    exit()


def get_plant_rank():

    print('-------- Plant Rank -------')
    
    for item in plant_data['data']:
        print(f'{item["common_name"]} Rank type is {item["rank"]}')

    print('------- End of Page -------')
    exit()


def run():
    display_main_menu()
    option = int(input("Enter option : "))
    if option == 1:
        get_plant_name()
    elif option == 2:
        get_plant_year()
    elif option == 3:
        get_plant_rank()


if __name__ == '__main__':
    run()

