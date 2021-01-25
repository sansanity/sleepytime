import datetime
import time
from datetime import datetime, timedelta

def wake_time(inp):
    pass




hours_cycle = 1
minutes_cycle = 30

while True:
    test = input("Enter a time in HH:MM format here:")

    try:
        hour, minute = [int(i) for i in test.split(":")]
        delta = timedelta(hours = hour, minutes = minute)
        print("Success!")
        print(delta)
    except:
        continue

# Find some way to make the time input stricter


# while True:
#     user_input = input("""
# This script shows you the optimal duration to sleep for.

# Type in:

# "a" if you want to choose your what time to wake up at

# "b" if you want to choose what time to fall asleep at

# "c" if you were to fall asleep right now


# """)
#     if user_input == "a":
#         wake_input = input("What time do you want to wake up at? ")

#     elif user_input == "b":
#         sleep_input = input("""
# What time will you fall asleep at?
# Note: A human being takes on average 12 minutes to fall asleep 
#         """)

#     elif user_input == "c":
#         pass

#     else:
#         continue