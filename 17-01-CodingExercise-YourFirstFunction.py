from random import random
from math import floor

def make_noise():
    print("THE CROWD GOES WILD")

make_noise()

def coin_flip():
    x = floor(random()*2)
    if x == 0:
        print("Head")
    else:
        print("Tail")

coin_flip()
