def perform_operation (num1, num2, operation ):
  if operation == "add":
    return num1 + num2
  elif opration == "subtract":
    return num1 - num2
  elif opration == "multiply":
    return num1 * num2
  elif opration == "divide":
    if num2 != 0 :
      return num1 / num2
    else:
      return "error"
    
  
