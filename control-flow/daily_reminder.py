# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task with match case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

# Adjust message if task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    elif priority == "medium":
        message += ". Try to schedule some time for it soon."

# Print the customized reminder
print(message)
