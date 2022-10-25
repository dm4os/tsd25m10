import random

'''
System description:
* streets have signs to make drivers aware about the speed limit.
    if I have a LIST of speed ranges then I would use a python list.

    Speed ranges are:
    * 0 [0...30]km/h
    * 1 [30...50]km/h
    * 2 [50...60]km/h
    * 3 [60...80]km/h
    * 4 [80...100]km/h
    * 5 [100...120]km/h

'''

speed_ranges = [0, 1, 2, 3, 4, 5]

#print(speed_ranges)

#function to simulate speed limits

def set_speed(somerange):
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


def set_speed_limit(limit):
    match limit:
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

def print_speed_limit(value):
    print("Current speed limit -> ", set_speed_limit(value))


#print(set_speed(5))

def important_loop():
    count = 0

    while True:
        random_speed_rng_gen = random.randint(0, 5)
        print("Current speed range -> ", random_speed_rng_gen)

        count += 1

        if count == 100:
            break

print_speed_limit(random.randint(0,5))