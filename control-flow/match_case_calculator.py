Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
  case "+":
    result = num1 + num2
  case "-":
    result = num1 - num2
  case "*":
    result = num1 * num2
  case "/":
    if num2 == 0:
      print("Cannot divide by zero.")
    else:
      result = num1 / num2
