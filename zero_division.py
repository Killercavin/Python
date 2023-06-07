a = 0
b = 5
try:
    c = (b/a)
except:
    print("Dividing a digit by zero will raise ZeroDivisionError so avoid it to prevent conflict between you and  python!")

''' Try-except block prevents python from raising conflicts by letting python follow what you tell it in the program '''

""" The except block informs python on how to respond to the error raised... """

''' The same happens with other errors like FileNotFoundError etc'''