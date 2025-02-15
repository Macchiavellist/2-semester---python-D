from datetime import datetime, timedelta

def Subtract():
    current_date = datetime.now()
    five_days_ago = current_date - timedelta(days=5)
    print("Current Date:", current_date)
    print("Five Days Ago:", five_days_ago)

def threedayc():
    current_date = datetime.now()
    yesterday = current_date - timedelta(days=1)
    tomorrow = current_date + timedelta(days=1)
    print("\nYesterday:", yesterday)
    print("Today:", current_date)
    print("Tomorrow:", tomorrow)

def microcek():
    current_datetime = datetime.now()
    current_datetime_no_microseconds = current_datetime.replace(microsecond=0)
    print("\nDatetime with microseconds:", current_datetime)
    print("Datetime without microseconds:", current_datetime_no_microseconds)

def difference():
    date_1 = datetime(2025, 2, 16, 10, 30, 0)
    date_2 = datetime(2025, 2, 16, 12, 45, 30)
    difference = date_2 - date_1
    difference_in_seconds = difference.total_seconds()
    print("\nDifference between date_2 and date_1 in seconds:", difference_in_seconds)

# Take user input to decide which function to execute
xdd = input("Enter a function name (Subtract, threedayc, microcek, difference): ")

if xdd == "Subtract":
    Subtract()
elif xdd == "threedayc":
    threedayc()
elif xdd == "microcek":
    microcek()
elif xdd == "difference":
    difference()
else:
    print("Invalid function name entered.")
