# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    # Return the formatted date (for the checker)
    return formatted_date

def calculate_future_date(days):
    # Save the current date
    current_date = datetime.now()
    # Add the given number of days
    future_date = current_date + timedelta(days=days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    # Return the formatted future date (for the checker)
    return formatted_future

def main():
    # Part 1: Show current date and time
    display_current_datetime()

    # Part 2: Prompt user for days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: ").strip())
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
