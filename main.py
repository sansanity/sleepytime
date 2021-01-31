import datetime
import time
from datetime import datetime, timedelta


one_cycle = timedelta(hours = 1, minutes = 30)
fall_asleep = timedelta(minutes = 15)


def wake_time():
    while True:
        try:
            time = datetime.strptime(input("Specify your wake time in HH:MM format: "), "%H:%M")
            for i in range(1,7):
                    cycle_hour = (time - one_cycle * i).hour
                    cycle_minute = (time - one_cycle * i).minute
                    if cycle_hour == 0:
                        cycle_hour = "00"
                    if cycle_minute == 0:
                        cycle_minute = "00"
                    print(f"In order to obtain {i} sleep cycle's worth of sleep, set your alarm at {cycle_hour}:{cycle_minute}")
        except:
            raise Exception("Please enter according to the given format HH:MM")


def fall_asleep_time():
    while True:
        try:
            time = datetime.strptime(str(input("Specify your sleep time in HH:MM format: ")), "%H:%M")
            for i in range(1,7):
                    cycle_hour = (time + one_cycle * i).hour
                    cycle_minute = (time + one_cycle * i).minute
                    if cycle_hour == 0:
                        cycle_hour = "00"
                    if cycle_minute == 0:
                        cycle_minute = "00"
                    print(f"In order to obtain {i} sleep cycle's worth of sleep, set your alarm at {cycle_hour}:{cycle_minute}")        
        except:
            raise Exception("Please enter according to the given format HH:MM: ")


def fall_asleep_now():
    time = datetime.now()
    time += fall_asleep # Accounts for the time it takes to fall asleep on average (15 minutes after the current time)
    for i in range(1,7):
        cycle_hour = (time + one_cycle * i).hour
        cycle_minute = (time + one_cycle * i).minute
        if cycle_hour == 0:
            cycle_hour = "00"
        if cycle_minute == 0:
            cycle_minute = "00"
        if len(str(cycle_minute)) == 1:
            str(cycle_minute)
            cycle_minute = "0" + cycle_minute
        print(f"In order to obtain {i} sleep cycle's worth of sleep, set your alarm at {cycle_hour}:{cycle_minute}")  


while True:
    user_input = input("""
This script shows you the optimal duration to sleep for.

Type in:

"a" if you want to choose your what time to wake up at

"b" if you want to choose what time to fall asleep at

"c" if you were to fall asleep right now


""")
    if user_input == "a":
        wake_time()

    elif user_input == "b":
        fall_asleep_time()

    elif user_input == "c":
        fall_asleep_now()
        break

    # else:
    #     continue