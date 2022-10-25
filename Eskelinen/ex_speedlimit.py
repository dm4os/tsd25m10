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
speed_range_values = [30, 50, 60, 80, 100, 120]

# Return a random speed limit from the range of speed limits
def randomSpeedLimit():
    return random.choice(speed_range_values)

print(randomSpeedLimit())

# I don't see how this is supposed to be done with 2 separate functions or using the original range/function.
# I also first did not understand that the speed limit should be random, that's why took so long to commit