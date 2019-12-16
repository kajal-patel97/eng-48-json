import requests
import json


def dictionary_postcode():
    pc1 = input('Please enter your first postcode?')
    pc2 = input('Please give a second postcode?')
    pc3 = input('Finally, enter the last postcode!')
    dict_pc = {
        'postcodes': [f'{pc1}', f'{pc2}', f'{pc3}']
    }

    # pass this into a dictionary
    json_body = json.dumps(dict_pc)

    # create the URL
    base_url = 'http://api.postcodes.io/'
    path = 'postcodes/'

    headers = {'Content-type': 'application/json'}

    postcode_post_response = requests.post(base_url + path, data=json_body, headers=headers)

    results = postcode_post_response.json()['result']

    for request in results:
        print(f"-- Postcode: {request['result']['postcode']}. NHS Location:{request['result']['nhs_ha']}")
    return 'Completed'


print(dictionary_postcode())
