def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator / denominator

    except ZeroDivisionError :
        return "Error: Cannot divide by zero."
    except ValueError :
        return "Error: Please enter numeric values only."
    except TypeError :
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"
    


