#!/usr/bin/env python
import time
import random
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

color = (90, 0, 90)
pos = random.randint(0, 63)
oldpos = 0

# 0 1 2
# 3 x 4
# 5 6 7

def print_pos(position):
    sense.set_pixel((position % 8), (position / 8), *color)
    return

def clear_pos(position):
    sense.set_pixel((position % 8), (position / 8), 0, 0, 0)
    return

print_pos(7)
