#!/usr/bin/env python
from __future__ import division
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(0)
sense.clear()
def wl_to_rgb(wl):
    #max wl - 780
    #min wl - 380
    gamma = 0.80
    max_intensity = 255

    if((wl >= 380) & (wl<440)):
        red = -(wl - 440) / (440 - 380)
        green = 0.0
        blue = 1.0
    elif((wl >= 440) & (wl<490)):
        red = 0.0
        green = (wl - 440) / (490 - 440)
        blue = 1.0
    elif((wl >= 490) & (wl<510)):
        red = 0.0
        green = 1.0
        blue = -(wl - 510) / (510 - 490)
    elif((wl >= 510) & (wl<580)):
        red = (wl - 510) / (580 - 510)
        green = 1.0
        blue = 0.0
    elif((wl >= 580) & (wl<645)):
        red = 1.0
        green = -(wl - 645) / (645 - 580)
        blue = 0.0
    elif((wl >= 645) & (wl<781)):
        red = 1.0
        green = 0.0
        blue = 0.0
    else:
        red = 0.0
        green = 0.0
        blue = 0.0

    # Let the intensity fall off near the vision limits

    if((wl >= 380) & (wl<420)):
        factor = 0.3 + 0.7 * (wl - 380) / (420 - 380)
    elif((wl >= 420) & (wl<701)):
        factor = 1.0
    elif((wl >= 701) & (wl<781)):
        factor = 0.3 + 0.7 * (780 - wl) / (780 - 700)
    else:
        factor = 0.0

    rgb = [0, 0, 0]

    # Don't want 0^x = 1 for x <> 0
    if red == 0.0:
        rgb[0] = 0
    else:
        rgb[0] = int(round(max_intensity * pow(red * factor, gamma)))
    if green == 0.0:
        rgb[1] = 0
    else:
        rgb[1] = int(round(max_intensity * pow(green * factor, gamma)))
    if blue == 0.0:
        rgb[2] = 0
    else:
        rgb[2] = int(round(max_intensity * pow(blue * factor, gamma)))

    return rgb


while True:
    humidity = sense.get_humidity()
    wl = int((((humidity - 30 ) / .7) * 4) + 380)
    i = wl_to_rgb(wl)
    h = i
    g = [min(255, i[0] + 30), min(255, i[1] + 30), min(255, i[2] + 30)]
    f = [min(255, i[0] + 60), min(255, i[1] + 60), min(255, i[2] + 60)]
    e = [min(255, i[0] + 90), min(255, i[1] + 90), min(255, i[2] + 90)]


    image = [
    e,e,e,e,e,e,e,e,
    e,f,f,f,f,f,f,e,
    e,f,g,g,g,g,f,e,
    e,f,g,h,h,g,f,e,
    e,f,g,h,h,g,f,e,
    e,f,g,g,g,g,f,e,
    e,f,f,f,f,f,f,e,
    e,e,e,e,e,e,e,e,
    ]

    sense.set_pixels(image)

    time.sleep(0.001)

