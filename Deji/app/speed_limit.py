import random


speed_limits = [20,40,60,80,100,120]
print ("Speed Limit: " + str((speed_limits)))
rand_speed_limit = random.choice(speed_limits)
print ("Generated Speed Limit is: " + str (rand_speed_limit))
