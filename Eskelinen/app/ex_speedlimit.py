import random

'''
System description:
* streets have signs to make drivers aware about the speed limit. 
    If I have a LIST of speed ranges then I would use a python list.

    Speed range are: []
    * 0 [0..30]km/h
    * 1 [30..50]km/h
    * 2 [50..60]km/h
    * 3 [60..80]km/h
    * 4 [80..100]km/h
    * 5 [100..120]km/h

'''

speed_ranges =  [0, 1, 2, 3, 4, 5]

# Give the speedlimit based on the range value
def giveSpeedLimit(x):
    speed_range_values = [30, 50, 60, 80, 100, 120]
    if x in speed_ranges:
        return speed_range_values[x]
# Need to check how to handle errors

# Give a random speed limit
def randomSpeedLimit():
    return giveSpeedLimit(random.choice(speed_ranges)) # Using the list to avoid errors here

# print(randomSpeedLimit())

old_limit = 30 # A default when no speed limit is defined
new_limit = randomSpeedLimit()

# Car function that expresses the speed limits and the needed action
# TODO: Check how to do this with a Class and an Object
def car(new_limit):
    print("Old limit was", old_limit)
    print("New limit is", new_limit)
    if old_limit > new_limit:
        print("Slow down!")
    if old_limit < new_limit:
        print("Speed up!")
    if old_limit == new_limit:
        print("Keep this speed.")

for x in range(0,5):
    new_limit = randomSpeedLimit()
    car(new_limit)
    old_limit = new_limit