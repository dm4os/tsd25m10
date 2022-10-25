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

speed_limits =  [30, 50, 60, 80, 100, 120]

speed_limit = int
    
#   Randomize speed_limit and randomize driving speed from that speed-10
def find_speed_within_random_limit():
    global speed_limit
    speed_limit = random.choice(speed_limits)
    return random.randint(speed_limit-10, speed_limit)

ctr = 0

while  True: 
    print("Driving speed -> ", find_speed_within_random_limit())
    print("Current speed limit -> ", speed_limit)
    
    ctr += 1

    if ctr == 3:
        #   To simulate speed changes on a typical road, we run the process 3 times
        # TODO: Record necessary acceleration/deceleration
        break