# Lab 19 Rain Data

import requests
import re
import math

# use requests to get a file
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/mt_tabor.rain')
data = response.text

total_rainfall = re.findall(r'\d{2}-\w{3}-\d{4}\s+\d+', data)

# list of dictionaries
rainfalls = []
for index in range(len(total_rainfall)):
    total = total_rainfall[index].split()
    rainfall = {
        'date': total[0],
        'daily_total': total[1],
    }
    rainfalls.append(rainfall)
# print(rainfalls)

# turn daily total of rainfall into a list
daily = []
for index in range(len(rainfalls)):
    daily.append(int(rainfalls[index]['daily_total']))
print(daily)
# calculate the mean
mean = sum(daily) / len(rainfalls)

# calulate the variance
deviations = 0
for index in range(len(daily)):
    deviations += daily[index] - mean ** 2 
variance = deviations / len(daily)
# change to absolute value 
variance = abs(variance)
variance = math.sqrt(variance)

# find the day which had the most rain
most_rainfall = 0
for index in range(len(rainfalls)):
    if int(rainfalls[index]['daily_total']) > most_rainfall:
        most_rainfall = int(rainfalls[index]['daily_total'])
        date = rainfalls[index]['date']


print(f'''
Rain Data for Mt. Tabor Maintenance Yard Rain Gage
----------------------------------------------------
Total mean = {round(mean)}
Total variance = {round(variance)}
{date} had the most rainfall with {most_rainfall} inches.
''')

