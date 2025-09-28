FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    c_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {c_temp:.2f}°C")

def convert_to_fahrenheit(celsius):
    f_temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {f_temp:.2f}°F")

temp_convert = float(input("Enter the temperature to convert: "))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if choice == "F":
    convert_to_celsius(temp_convert)
elif choice == "C":
    convert_to_fahrenheit(temp_convert)
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
