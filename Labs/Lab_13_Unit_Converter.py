print("Lab 13: Unit Converter")

units = {
    'feet': 0.3048,
    'mile': 1609.34,
    'meter': 1.0,
    'kilometer': 1000.0,
}

# Version 3
units.update({
    'yard': 0.9144,
    'inch': 0.0254,
})

# Version 1
'''
while True:

    user = input(f'What is the distance in feet? ')

    user = float(user)

    total = user * 0.3048

    print(f'{user} feet is {total} meters')
'''

# Version 2

'''
while True:

    quantity = input(f'What is the distance? ')

    unit_name = input(f'what are the units?: ')

    distance = units[unit_name]

    quantity = float(quantity)

    # calculate the total
    total = quantity * distance

    print(f'{quantity} {unit_name} is {total} meters')
'''

# Version 4

while True:

    quantity = input(f'What is the distance? ')

    unit_name = input(f'what are the input units?: ')

    convert = input(f"what are the output units?: ")

    distance = units[unit_name]

    quantity = float(quantity)

    # calculate the total
    total = quantity * distance

    # convert input distance to output distance
    distance_2 = units[convert]

    new_total = total / distance_2 


    print(f'{quantity} {unit_name} is {new_total} {convert}')