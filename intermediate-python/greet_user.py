import json
file = 'username.json'
with open(file) as json_file:
    name = json.load(json_file)
print("Welcome back to our restaurant", name+".")