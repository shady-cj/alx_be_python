task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


message = f"'{task}' is a "
match priority:
    case "high":
        message += "high priority task"
    case "medium":
        message += "medium priority task"
    case "low":
        message += "low priority task"

if time_bound == "yes":
    message = "Reminder: " + message + " that requires immediate attention today!"
else:
    message = "Note: " + message + ". Consider completing it when you have free time."

print(message)
