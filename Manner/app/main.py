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

#print(speed_ranges[5]) #[0..5] but we have 6 values

# Create a function which simulates speed limits
def set_speed_limit(somerange):
    match somerange:
        case 0:
            #print(" I have identified this case")
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
    
# The variable used by the function 
#in_var = "I am the variable value"

# Excecute the function using print

#ctr = 0 # A counter
'''
# A while loop which could run forever if the counter and IF condition would not be defined
while  True: 
    random_speed_rng_gen = random.randint(0, 5)
    print("Current speed range -> ", random_speed_rng_gen)
    #print(set_speed_limit()
    
    ctr += 1  # I increment the counter by 1
    
    # if condition. Breaks <<while loop>> if ctr == 100
    if ctr == 100:
        break
'''

#TODO from 13:08 to 14:08
#Based on the function we have created you need to:
#1. Create a function which only returns SPEEDS LIMITS not intervals
#2. Create a 2nd function which takes that generated SPEED LIMIT and returns it.
#    example-> def myfunc(theGenSpeedLimit):
#                    return (theGenSpeedLimit)
#3. print the returned value of the executed function on step 2

speed_limits = [20, 30, 40, 50, 60, 70, 80, 100, 120] 
def set_a_speed_limit():
    
    return random.choice(speed_limits)

def print_speed():
    current_speed = set_a_speed_limit()
    return current_speed

print(f"Current speed limit is {print_speed()}")
