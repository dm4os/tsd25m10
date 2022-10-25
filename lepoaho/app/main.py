import random

speed_limits =  [30, 50, 60, 80, 100, 120] 


def set_speed_limit(speed_limit_list):
    return speed_limit_list[random.randint(0,5)]
    

def return_speed_limit():
    gen_speed_limit = set_speed_limit(speed_limits)
    return gen_speed_limit

print(return_speed_limit())