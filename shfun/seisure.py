#!/usr/bin/env python
import random
import time
from sense_hat import SenseHat


sense = SenseHat()
sense.set_rotation(0)
sense.clear()

previous_pixel = (0, 0)
while True:
    x = int(random.getrandbits(3))
    y = int(random.getrandbits(3))
    r = int(random.getrandbits(8))
    g = int(random.getrandbits(8))
    b = int(random.getrandbits(8))
    #r = 255
    #g = 255
    #b = 255

    sense.set_pixel(*(previous_pixel + (0, 0, 0)))
    sense.set_pixel(x, y, r, g, b)
    previous_pixel = (x, y)
    time.sleep(0.01)
