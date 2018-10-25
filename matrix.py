#!/usr/bin/env python
import time
import random

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

length = 6  # length of the tail
color = 150  # shade of green from 0 - 255
randomness = 12  # lower number = more dense
sleep = 0.05  # lower number = faster

matrix = [[[0, 0] for y in range(8)] for x in range(8)]

while True:
    for row in range(8):
        if row == 0:
            for col in range(8):
                if not matrix[row][col][0] and not random.randint(0, randomness):
                    matrix[row][col] = [1, 0]
                    sense.set_pixel(col, row, int(color * 0.5), color, int(color * 0.5))
                elif matrix[row][col][0] == 1 and matrix[row][col][1] < length:
                    matrix[row][col][1] += 1
                    sense.set_pixel(col, row, 0, color, 0)
                elif matrix[row][col][0] == 1 and matrix[row][col][1] == length:
                    matrix[row][col][1] += 1
                    sense.set_pixel(col, row, 0, int(color * 0.5), 0)
                else:
                    matrix[row][col] = [0, 0]
                    sense.set_pixel(col, row, 0, 0, 0)
        else:
            for col in range(8):
                if not matrix[row][col][0] and matrix[row - 1][col] == [1, 0]:
                    pass
                elif matrix[row][col][0] == 0 and matrix[row - 1][col][0] == 1:
                    matrix[row][col] = [1, 0]
                    sense.set_pixel(col, row, int(color * 0.5), color, int(color * 0.5))
                elif matrix[row][col][0] == 1 and matrix[row][col][1] < length:
                    matrix[row][col][1] += 1
                    sense.set_pixel(col, row, 0, color, 0)
                elif matrix[row][col][0] == 1 and matrix[row][col][1] == length:
                    matrix[row][col][1] += 1
                    sense.set_pixel(col, row, 0, int(color * 0.5), 0)
                else:
                    matrix[row][col] = [0, 0]
                    sense.set_pixel(col, row, 0, 0, 0)

    time.sleep(sleep)

