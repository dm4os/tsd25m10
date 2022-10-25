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


def set_speed_limit():
    limits = [30,50,60,80,100,120]
    return random.choice(limits)

def return_speed_limit():
    return set_speed_limit()

def set_speed_based_on_limit(limit):
    match limit:
        case 30:
            return set_speed(0)
        case 50:
            return set_speed(1)
        case 60:
            return set_speed(2)
        case 80:
            return set_speed(3)
        case 100:
            return set_speed(4)
        case 120:
            return set_speed(5)


#print(set_speed(5))

def important_loop():
    count = 0

    while True:
        random_speed_rng_gen = random.randint(0, 5)
        print("Current speed range -> ", random_speed_rng_gen)

        count += 1

        if count == 100:
            break

#print("Current speed limit -> ", return_speed_limit())

#print("Current speed based on limit -> ", set_speed_based_on_limit(return_speed_limit()))


def print_limit_and_speed():
    currentLimit = return_speed_limit()
    print("Current speed limit: ", currentLimit, "km/h")
    print("Current speed based on limit: ", set_speed_based_on_limit(currentLimit), "km/h")
    newLimit = return_speed_limit()
    if newLimit > currentLimit:
        print("New limit ", newLimit, "km/h is higher, adjust speed")
        print("Current speed based on limit: ", set_speed_based_on_limit(newLimit), "km/h")
    elif newLimit < currentLimit:
        print("New limit ", newLimit, "km/h is lower, adjust speed")
        print("Current speed based on limit: ", set_speed_based_on_limit(newLimit), "km/h")
    else:
        print("same limit, run agains")
        print_limit_and_speed()


print_limit_and_speed()