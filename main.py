import datetime
import time
from datetime import datetime, timedelta


one_cycle = timedelta(hours = 1, minutes = 30)


def wake_time():
    while True:
        try:
            time = datetime.strptime(input("Specify your wake time in HH:MM format: "), "%H:%M")
    

def fall_asleep_time():
    while True:
        try:
            time = datetime.strptime(str(input("Specify your sleep time in HH:MM format: ")), "%H:%M")
            for i in range(1,7):
                print(f"In order to obtain {i} sleep cycle's worth of sleep, set your alarm at {time + one_cycle * i}")
        except:
            raise Exception("Please enter according to the given format HH:MM: ")


def fall_asleep_now():
    time = datetime.now()
    for i in range(1,7):
        print(f"In order to obtain one sleep cycle's worth of sleep, set your alarm at {time + one_cycle * i}")


# Remove year from the timedelta output




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