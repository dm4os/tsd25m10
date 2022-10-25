import random

'''
System description:
* 
    ### TODO from 13:08 to 14:08
Based on the function we have created you need to:
1. Create a function which only returns SPEEDS LIMITS not intervals
2. Create a 2nd function which takes that generated SPEED LIMIT and returns it.
    example-> def myfunc(theGenSpeedLimit):
                    return (theGenSpeedLimit)
3. print the returned value of the executed function on step 2

complete a program where an speed limit is randomly generated 
and a function simulating a car response adapting to a certain speed limit.

Basically the "car" function would have 2 states old and current speed. 
The function would take the new speed limit, 
compared to the old one and print old and new speed limit.


'''

speed_limits =  [30, 50, 60, 80, 100, 120] # List contains 6 speed limit values
car_old_speedlimit = 0


# function that sets the speed limit randomly to one of the values from the speed limits table
# parameter: list of speed limits
def set_speed_limit(speed_limit_table):
    return speed_limit_table[random.randint(0,5)]
    
# function that calls the speed limit setting function and returns the speed limit
# 
def return_speed_limit():
    generated_speed_limit = set_speed_limit(speed_limits)
    return generated_speed_limit

# function for setting the value of the old speed limit
def set_old_speed_limit(oldspeedlimit):
    global car_old_speedlimit 
    car_old_speedlimit = oldspeedlimit

# function for getting the old speed limit
def return_car_old_speedlimit():
    return car_old_speedlimit

# function for simulating a car driving
# 
def simulate_car():
    new_speed_limit = return_speed_limit()
    old_speed_limit = return_car_old_speedlimit()
    print("Speed limit changes.")
    print("Old speed limit was " + str(car_old_speedlimit))
    print("New speed limit is " + str(new_speed_limit))
    if(old_speed_limit < new_speed_limit):
        print("Increasing car speed by " + str(new_speed_limit - old_speed_limit) + " km/h to match the new speed limit.")
    elif(old_speed_limit > new_speed_limit):
        print("Slowing down by " + str(old_speed_limit - new_speed_limit) + " km/h to match the new speed limit.")
    else:
        print("Speed limit stayed the same, continuing with the same speed.");
    set_old_speed_limit(new_speed_limit)



counter = 0

while counter < 10:
    simulate_car()
    counter += 1