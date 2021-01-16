print("Lab 19: Rain Data")

import re
import json
import datetime
import requests
import statistics


### Version 1 ###

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')


# download files
with open('Hayden_Island_Rain_Data.txt', 'r') as file:
    text = file.read()

# parse data (extract date and daily totals of rain fall)
daily_hourly_data = re.findall(r'\d{2}-\w{3}-\d{4}\s+\d+', text)

# turn a string into a datetime object
def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%d-%b-%Y')

# create a dictionary to display the amount of rain per day
rain_data = []
for index in range(len(daily_hourly_data)):
    rain_data_breakdown = daily_hourly_data[index].split()
    rain_data_2 = {
        'date_of_rain': rain_data_breakdown[0],
        'rain_tally': rain_data_breakdown[1]
    }
    rain_data.append(rain_data_2)
    
        
### VERSION 2 ###
    
# merge individual strings('rain_tally' = rain_data_breakdown[1])  into a single list
rain_tally = []
for rain in range(len(rain_data)):
    rain_tally.append(int(rain_data[rain]['rain_tally']))


# calculate mean of daily rainfall totals    
mean = sum(rain_tally) / len(rain_data)
print(f"mean: {mean}")

# Use the mean to calculate the variance via list comprehension
variance = sum((number - mean) ** 2 for number in rain_tally) / len(rain_data)
print(f"variance: {variance}")   

# Loop over all the records to find the one which had the most rain
most_rain = 0
for rain in daily_hourly_data:
    if most_rain == 0 or rain_data_2['rain_tally'] > most_rain[0]:
        most_rain = rain

# print out the date and daily total to the user        
print(most_rain)
