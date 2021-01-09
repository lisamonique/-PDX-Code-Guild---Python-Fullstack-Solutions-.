import time

current_time = time.localtime()


while current_time.tm_year < 2021:
    current_time = time.localtime()

    current_day = current_time.tm_yday
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_time.tm_year% 4 ==0:
        days_remaining = str(366 -current_day)
    else:
        days_remaining = str(365 - current_day)

    
    hours_remaining = str(24 - current_hour)
    minutes_remaining = str(60 - current_minute)
    seconds_remaining = str(60 - current_second)


    print(f'{days_remaining.zfill(1)} day {hours_remaining.zfill(1)} hours {minutes_remaining.zfill(1)} minutes {seconds_remaining.zfill(1)} seconds')
    
    time.sleep(1)
print("Happy New Year!!!!")




'''
for i in range(10):
    countdown = 10 - i
    print(f"{str(countdown).zfill(2)}", end="\r")
    time.sleep(1)
'''