from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it nicely
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days):
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    # Step 1: Display current date/time
    current_date = display_current_datetime()
    
    # Step 2: Ask for number of days to add
    days = int(input("Enter the number of days to add to the current date: "))
    
    # Step 3: Calculate and display future date
    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()

