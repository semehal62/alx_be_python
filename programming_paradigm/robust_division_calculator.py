def safe_divide(numerator, denominator):
    float(numerator)
    float(denominator)
    try:
        result = numerator / denominator

    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError :
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {result}")
    


