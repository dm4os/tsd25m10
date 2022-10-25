import random

'''

System description:
* streets have signs to make drivers aware about their speed limit
    If I have a LIST of speed ranges then I would use a python list.

    Speed ranges are: [0]
    * 0 [0..30]km/h
    * 1 [30..50]km/h
    * 2 [50..60]km/h
    * 3 [60..80]km/h
    * 0 [80..100]km/h
    * 0 [100..120]km/h

'''

'''speed_ranges = [0, 1, 2, 3, 4, 5]

#Create a function which simulates speed limits
def set_speed_limit(somerange):
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
            return random.randint(100, 120)'''


speed_limits =  [30, 50, 60, 80, 100, 120] 


def set_speed_limit(speed_limit_list):
    return speed_limit_list[random.randint(0,5)]
    

def return_speed_limit():
    gen_speed_limit = set_speed_limit(speed_limits)
    return gen_speed_limit

print(return_speed_limit())
