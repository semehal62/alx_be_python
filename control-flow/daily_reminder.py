task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
  case "high" and time_bound == "yes":
            print("Reminder: ","'",tasl,"'", " is a high priority task that requires immediate attention today!")
  case "low" and time_bound == "yes":
             print("Reminder: ","'",tasl,"'", " is a low priority task that requires immediate attention today!")
  case "high" and time_bound == "no":
            print("Reminder: ","'",tasl,"'", " is a low priority task. Consider completing it when you have free time.")
  case "low" and time_bound == "no":
             print("Reminder: ","'",tasl,"'", " is a low priority task. Consider completing it when you have free time.")
