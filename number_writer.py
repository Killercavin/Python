import json

'''This very first phase of this program will focus on creating the json file and stores the number in the file'''
number = [2, 3, 5, 7, 11, 13]
file = 'number.json'
with open(file, 'w') as f:
    json.dump(number, f)

"""Thi second phase loads the previosly dumped json file and prints it out"""
with open(file) as myFile:
    number = json.load(myFile)
print(number)