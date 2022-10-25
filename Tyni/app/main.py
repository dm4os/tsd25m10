from asyncio.windows_events import NULL
import random
import time
from re import I
from time import sleep

'''
System description
* streets have signs to make drivers aware about the speed limit.
    If i have a LIST of speed ranges, then I would use a python list.

    Speed ranges are: 
    * 0 [0..30]km/h
    * 1 [30..50]km/h
    * 2 [50..60]km/h
    * 3 [60..80]km/h
    * 4 [80..100]km/h
    * 5 [100..120]km/h

'''

speed_ranges = [0, 1, 2, 3, 4, 5] #List contains 6 values which are from 0-5.
speed_limits = [30, 50, 60, 80, 100, 120] #List contains 6 speed limits 

#print(speed_ranges)

# Create a function which simulates the speed limits.

def set_speed_limits (somerange):
    match somerange:
        case 0:
            return random.randint(0, 30)
        case 1:
            return random.randint(30, 50)
        case 2:
            return random.randint(50, 60)
        case 3:
            return random.randint(60, 80)
        case 4:
            return random.randint(80, 100)
        case 5:
            return random.randint(100, 120)


def get_speed_limits (speed_limit_list):
    #Gets the speed limits list and returns one of them randomly
    return speed_limit_list[random.randint(0, 5)]

def return_speed_limit():
    #Returns the speed limit
    return get_speed_limits(speed_limits)


ctr = 0
lastlimit = 0

while True:
    adapt = 15
    random_speed_rng_gen = random.randint(0, 5) #Just a random int between 0 and 5
    currentlimit = return_speed_limit()
    #Here we print the max speed.
    print("The current speed limit is ", currentlimit, " and last speed limit was ", lastlimit)
    ctr += 1
    time.sleep(1)

    if lastlimit > currentlimit:
        print("Slowing down")
        lastlimit = currentlimit
    elif lastlimit < currentlimit:
        print("Speeding up")
        lastlimit = currentlimit
    else:
        print("Driving at same speed")
        lastlimit = currentlimit

    if ctr == 10:
        break



