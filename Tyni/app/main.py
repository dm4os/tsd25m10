import random

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
'''
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
'''

def get_speed_limits (speed_limit_list):
    #Gets the speed limits list and returns one of them randomly
    return speed_limit_list[random.randint(0, 5)]

def return_speed_limit():
    #Returns the speed limit
    return get_speed_limits(speed_limits)


#Here we print the max speed.
print("The max speed limit is ", return_speed_limit())

'''
# The variable used by the function
#in_var = "I am the variable value"

ctr = 0

# A while loop which could run forever if the counter and IF condition would not be defined

while True:
    random_speed_rng_gen = random.randint(0, 5) #Just a random int between 0 and 5

    #print("Current speed range is ", random_speed_rng_gen)

    #print(set_speed_limits())


    ctr += 1 # Adds 1 to ctr everytime this runs

    if ctr == 100: #When ctr reaches 100, application stops
        break
'''