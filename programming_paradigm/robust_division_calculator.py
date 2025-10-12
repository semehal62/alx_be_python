def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator

    except ZeroDivisionError as e:
        print(f"Error: cannot divied by zero.")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError :
        print(f"Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {result}")
    


