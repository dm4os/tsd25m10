'''
Case a. I will send a message to the ones who are coding better to complete a program where an speed 
limit is randomly generated and a function simulating a car response adapting to a certain speed 
limit.

Basically the "car" function would have 2 states old and current speed. The function would take 
the new speed limit, compared to the old one and print old and new speed limit.

# Speed controller of autonomous vehicles

## Behavior-driven development [BDD] approach
As a        driver
I WANT      the car to determine the speed limit and adjust the speed to that limit.
SO THAT     I don't have to adjust the speed myself

## Acceptance test-driven development [ATDD] approach
GIVEN       the speed limit 70km/h
WHEN        the car in moving
THEN        the speed limit should remain/adjusted between 65 and 70km/h

GIVEN       the speed limit 70km/h
WHEN        the speed limit changes to 50km/h
THEN        deceleration rate should be 15km/h(hvirtual) 

'''

import random

class Car:
  def __init__ (self, old_speed, current_speed):
    self.old_speed = old_speed
    self.current_speed = current_speed
    
  def accelerate(self, value):
    self.current_speed+= value
    print(f"Wroom! Too slow, accelerating by {value} km/h...")
    
  def decelerate(self, value):
    self.current_speed-= value
    print(f"Wroom! Too fast, decelerating by {value} km/h...")
    
  def drive(self):
    print("Wroom wroom. Driving along the speed limits.")


speed_limits =  [30, 50, 60, 80, 100, 120] # List contains 6 values which are counted from 0 to 5
randomized_speed_limits = [0, 0, 0, 0, 0, 0]

# initialize a new car

mycar = Car(0, 50)

# randomize the speed limit values
for i in range (0, len(speed_limits)):
  randomized_speed_limits[i] = speed_limits[random.randint(0,5)]

# "move" the car through the speed limit "zones"
for n in range (0, len(speed_limits)):
  
  if mycar.current_speed > randomized_speed_limits[n]:
    mycar.decelerate(15)
  elif mycar.current_speed < randomized_speed_limits[n]:
    mycar.accelerate(15)
  else:
    mycar.drive()
    
    

