task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
  case x if x == "high" and time_bound == "yes":
            print("Reminder: ","'",tasl,"'", " is a high priority task that requires immediate attention today!")
  case x if x == "low" and time_bound == "yes":
             print("Reminder: ","'",tasl,"'", " is a low priority task that requires immediate attention today!")
  case x if x == "high" and time_bound == "no":
            print("Reminder: ","'",tasl,"'", " is a low priority task. Consider completing it when you have free time.")
  case x if x == "low" and time_bound == "no":
             print("Reminder: ","'",tasl,"'", " is a low priority task. Consider completing it when you have free time.")
