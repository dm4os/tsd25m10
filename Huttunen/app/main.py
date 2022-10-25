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

speed_ranges =  [30, 50, 60, 80, 100, 120] 


def get_speed_limit(limit):
    return random.choice(limit)

def return_limit():
  return get_speed_limit(speed_ranges)

i = 1
while i < 6:
    print(return_limit())
    i += 1