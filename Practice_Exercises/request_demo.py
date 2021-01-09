import requests
import json

'''
response = requests.get("https://google.com")

print(response)

print(response.__dict__.keys())

print(response.text)
'''
#-------------------------------------------------------------#

response = requests.get("https://jsonplaceholder.typicode.com/users/")

#print(response)

#print(response.text)

#print(type(response.text))

data = json.loads(response.text)

#print(data)

for user in data:
    print(user['name'])
    print(user['email'])
    print(user['phone'])
    print('-'*12)
'''
#-------------------------------------------------------------------#

response = requests.get("https://jsonplaceholder.typicode.com/post/")
data = json.loads(response.text)

for post in data:
    print(post['title'])
    print()
'''