def safe_divide(numerator, denominator):
    float(numerator)
    float(denominator)
    try:
        result = numerator / denominator

    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
    except ValueError as e:
        return f"Error: {e}"
    except TypeError :
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"
    


