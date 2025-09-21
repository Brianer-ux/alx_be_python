# control-flow/daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unspecified priority level"

# Add urgency if time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif priority == "low":
    message += ". Consider completing it when you have free time."

print(message)
