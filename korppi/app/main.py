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

speed_ranges =  [0, 1, 2, 3, 4, 5] # List contains 6 values which are counted from 0 to 5

# a function to get actual speed limits in km/h.
def get_speed_limits(range):
  match range:
    case 0: return 30
    case 1: return 50
    case 2: return 60
    case 3: return 80
    case 4: return 100
    case 5: return 120

def get_speedlimit(spdlimit):
  return get_speed_limits(spdlimit)


for i in range (0, len(speed_ranges)):
  print(get_speedlimit(i))

