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

'''

speed_limits =  [30, 50, 60, 80, 100, 120] # List contains 6 speed limit values

# function that sets the speed limit randomly to one of the values from the speed limits table
# parameter: list of speed limits
def set_speed_limit(speed_limit_table):
    return speed_limit_table[random.randint(0,5)]
    
# function that calls the speed limit setting function and returns the speed limit
# 
def return_speed_limit():
    generated_speed_limit = set_speed_limit(speed_limits)
    return generated_speed_limit

print("Speed limit is: ")
print(return_speed_limit())