guest_file = 'guest.txt'
with open(guest_file, 'a') as file_object:
    name = str(input("Enter your name: "))
    file_object.write(name)