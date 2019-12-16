import json

#defining the dictionary
car_dictionary = {
    'name': 'tesla',
    'engine': '90000kw',
    'type': 'engine'
}
# this prints out the type -- which shows that it is a dictionary
#print(type(car_dictionary))

# # this prints out the whole dictionary, with keys and entry
# print(car_dictionary)

# To create a JSOn string from our dictionary
car_data_json_string = json.dumps(car_dictionary)

# #the type should be a string now
# print(type(car_data_json_string))

#json.dump --> writes json to a file
#the new file will be created 'new_json_file.json'

# with open('new_json_file.json', 'w') as jsonfile:
#     json.dump(car_dictionary, jsonfile)


#json.load(jsonfile) ---> dictionary
# Loads it as a dictionary to read it again

with open('new_json_file.json', 'r') as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car['engine']) # this gets the value of the cars engine in the dictionary