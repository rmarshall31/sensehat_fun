#!/usr/bin/env python
import time
import random
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

color = (30, 0, 150)
pos = random.randint(0, 63)
oldpos = 0
flower = random.randint(0, 63)

# 0 1 2
# 3 x 4
# 5 6 7

def print_pos(position, color):
    sense.set_pixel((position % 8), (position / 8), *color)
    return

def clear_pos(position):
    sense.set_pixel((position % 8), (position / 8), 0, 0, 0)
    return

print_pos(flower, (90, 90, 0))

while True:
    moved = False
    clear_pos(oldpos)
    if flower == oldpos:
        flower = random.randint(0, 63)
        print_pos(flower, (90, 90, 0))
    oldpos = pos
    print_pos(pos, color)
    while moved is False:
        move = random.randint(0, 7)
        if move == 0:
            if pos not in [(y * 8) for y in range(8)] and pos not in range(8):
                pos -= 9
                moved = True
        if move == 1:
            if pos not in range(8):
                pos -= 8
                moved = True
        if move == 2:
            if pos not in [(y * 8) + 7 for y in range(8)] and pos not in range(8):
                pos -= 7
                moved = True
        if move == 3:
            if pos not in [y*8 for y in range(8)]:
                pos -= 1
                moved = True
        if move == 4:
            if pos not in [(y * 8) + 7 for y in range(8)]:
                pos += 1
                moved = True
        if move == 5:
            if pos not in [(y * 8) for y in range(8)] and pos not in [(y + 56) for y in range(8)]:
                pos += 7
                moved = True
        if move == 6:
            if pos not in [(y + 56) for y in range(8)]:
                pos += 8
                moved = True
        if move == 7:
            if pos not in [(y + 56) for y in range(8)] and pos not in [(y * 8) + 7 for y in range(8)]:
                pos += 9
                moved = True

    time.sleep(0.05)

