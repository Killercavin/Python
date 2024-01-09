filename = 'py.txt'
with open(filename) as my_file:
    lines = my_file.readlines()
    for line in lines:
        print(line.rstrip())