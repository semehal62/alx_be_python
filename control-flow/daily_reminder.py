task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match time_bound:
  case x if x == "yes" and priority == "high":
            print("Reminder: ","'",tasl,"'", " is a high priority task that requires immediate attention today!")
  case x if x == "yes" and priority == "low":
             print("Reminder: ","'",tasl,"'", " is a low priority task that requires immediate attention today!")
  case x if x == "no" and priority == "high":
            print("Reminder: ","'",tasl,"'", " is a low priority task. Consider completing it when you have free time.")
  case x if x == "no" and priority == "low":
             print("Reminder: ","'",tasl,"'", " is a low priority task. Consider completing it when you have free time.")
