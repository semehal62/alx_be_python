def safe_divide(numerator, denominator):
    numerator = float(numerator)
    deniminator = float(denominator)
    try:
        result = numerator / denominator

    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
    except ValueError as e:
        return "Error: Please enter numeric values only."
    except TypeError :
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"
    


