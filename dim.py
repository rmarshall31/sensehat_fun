#!/usr/bin/env python
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.clear()

sleep = 0.1

while True:
    for i in range(256):
        e = [i, i, i]
        print i
        image = [
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        ]

        sense.set_pixels(image)

        time.sleep(sleep)

    for i in range(256):
        e = [255 - i, 255 - i, 255 - i]
        print 255 - i
        image = [
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        ]

        sense.set_pixels(image)

        time.sleep(sleep)

