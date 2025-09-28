FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
  c_temp = FAHRENHEIT_TO_CELSIUS_FACTOR *(fahrenheit -32)
  print(f"{fahrenheit} is {c_temp}" )
def convert_to_fahrenheit(celsius) :
  f_temp = ( CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) +32
  print(f"{celsius} is {c_temp}" )
temp_convert = input("Enter the temperature to convert: ")
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if choice == "F":
  convert_to_celsius(temp_convert)
elif choice == "C"
  convert_to_fahrenheit(temp_convert)
