with open('py.txt') as file_object:
    contents = file_object.read()
    '''for line in contents: 
        print(line)''' # this will get each line of the file to be read
print(contents)
print(contents.count('ipsum')) 
'''.count(x) takes atleast one agument and can be used to get the number of times a word or digit appears....'''
