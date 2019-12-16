import requests
# Get requests
# They do not have a body (json)
# They have a base url, path and argument

# api.postcodes.oi/postcodes --> this url contains a base url and a path

base_url = 'http://api.postcodes.io/'
path = 'postcodes/'
arguments = 'e146gt'

request_response = requests.get(base_url + path + arguments)

#turn it into a dictionary
dictionary_response = request_response.json()

print(dictionary_response)
print(dictionary_response['result']['admin_ward'])