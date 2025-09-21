task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

message = f"Note: '{task}' is a {priority} priority task."

# Use a match statement to create the base message based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unspecified priority level"

# Use an if/else block to modify the message based on time-bound status
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif priority == "low" and time_bound == "no":
    message += ". Consider completing it when you have free time."

print(message)
