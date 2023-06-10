cat_dog = ['cat.txt', 'dog.txt', 'foo']
for file in cat_dog:
    try:
        with open(file) as fileObject:
            myFile = fileObject.read()
    except FileNotFoundError as e:
        print(f"File {cat_dog.__getitem__(2)} not found or unaccessible due to security measures.") # Specified the unaccessible or the file that wasn't found using the .__getitem__() methpd in lists
        '''We use the pass function to silenty fail the exception'''
        """If you intend to modify this file so that the exception fails silently just replace the code below with the innitial prit(f"File ...")"""
        # pass 
    else:
        print(file)

