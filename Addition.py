print("Provide me with two numbers and I will sum them up.")

while bool(1):
    num1 = input("Enter the value of num1: ")
    num2 = input("Enter the value of num2: ")
    if num1 or num2 == int:
        try:
            sum = int(num1) + int(num2)
        except ValueError:
            print("One of the values you've enter ain't an integer so, I have a problem in determing the sum!")
    else:
        print("The sum of num1 and num2 is: ",sum)
