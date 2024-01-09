import json
username = str(input("Enter your username: ")) # gets the user input requesting for his/her username
file_name = 'username.json' # innitializing our file_name variable with a file named username.json
with open(file_name, 'w') as my_file: # will write files to the destination file created
    json.dump(username, my_file) # will save the changes or odifications made n the file
print(f"{username}, we'll remember you when you get back, see you on your next visit to our restaurant...")
