number1 = float(input("enter first number: "))
number2 = float(input("enter second number:"))

print("choose an operation: + - * /")
operation = input("enter operation:")

if operation == "+":
 result = number1 + number2
 print("the result is:", result)
 
elif operation == "-":  
 result = number1 - number2 
 print("the result is:" , result)

elif operation =="*":
 result = number1 * number2
 print("the result is:", result)

elif operation =="/":
  if number2 != 0:
    result = number1 / number2
    print("the result is:", result)
  else:
    print("Error: Division by zero is not allowed.")