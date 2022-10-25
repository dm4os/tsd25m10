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
#speed_range_values = [30, 50, 60, 80, 100, 120]

# Give the speedlimit based on the range value
def giveSpeedLimit(range):
    match range:
        case 0:
            return 30
        case 1:
            return 50
        case 2:
            return 60
        case 3:
            return 80
        case 4:
            return 100
        case 5:
            return 120

# Give a random speed limit
def randomSpeedLimit():
    return giveSpeedLimit(random.choice(speed_ranges))

print(randomSpeedLimit())

# I don't see how this is supposed to be done with 2 separate functions or using the original range/function.
# I also first did not understand that the speed limit should be random, that's why took so long to commit