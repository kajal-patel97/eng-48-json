import requests
import json

# Making a Post request

#We need a path
# We need a JSON object to send
# Possibly headers depending on the API

# Creating the JSON
dictionary_post_codes = {
    'postcodes': ['EC2Y 5AS', 'e146gt', 'CT1 2EH'] # Make sure postcodes is written the same as http://postcodes.io/
}

# Pass in our dictionary for JSON
json_body = json.dumps(dictionary_post_codes)

# The URL
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

#Headers are the core part of HTTP requests and the responses, they carry information about the client browser, requested page, server and more

## The header
headers = {'Content-type': 'application/json'}

#making the request --  this passes in the data
postcodes_post_response = requests.post(base_url + path, data=json_body,headers= headers)

# This prints with the code 200 which means it is successful and running
print(postcodes_post_response)

results = postcodes_post_response.json()['result']

for request in results:
    print(request['result']['nhs_ha'])