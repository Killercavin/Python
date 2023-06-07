print("Give me two numbers, and I'll divide them.")
print("Enter 'q' or 'e' to quit.")

while True:
  first_number = input("\nFirst number: ")
  if first_number == 'q' or 'e':
   break
  
  second_number = input("Second number: ")
  if second_number == 'q' or 'e':
   break
   
  try:
    answer = int(first_number) / int(second_number)
  except ZeroDivisionError:
    print("You can't divide by zero.")

  else:
    print(answer)