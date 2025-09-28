from datetime import datetime, date, time, timedelta
def display_current_datetime ():
  current_date = datetime.now()
  print(f"Current date and time: { current_date} ")
def calculate_future_date ():
  number = input("Enter the number of days to add to the current date: ")
  future_date = date.today()
   future_date += number

  print(f"Future date: {future_date}")
