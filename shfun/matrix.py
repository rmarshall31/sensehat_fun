#!/usr/bin/env python
import random
import time

from sense_hat import SenseHat


class Matrix:
    """displays a matrix-like visual effect on the sense hat
    Attributes:
        rotation    how is your pi oriented?
        length      length of the tail
        color       shade of green from 0 - 255
        randomness  lower number = more dense
        refresh     lower number = faster
        cycles      how many cycles to do (0 to run forever)
    """

    def __init__(
            self,
            rotation=0,
            length=6,
            color=150,
            randomness=12,
            refresh=0.05,
            cycles=0,
    ):
        self.length = length
        self.color = color
        self.randomness = randomness
        self.refresh = refresh
        self.cycles = cycles

        self.sense = SenseHat()
        self.sense.set_rotation(rotation)
        self.sense.clear()

        self.matrix = [[[0, 0] for y in range(8)] for x in range(8)]

    def enter(self):
        completed_cycles = 0
        while True:
            for row in range(8):
                if row == 0:
                    for col in range(8):
                        if not self.matrix[row][col][0] and not random.randint(0, self.randomness):
                            self.matrix[row][col] = [1, 0]
                            self.sense.set_pixel(col, row, int(self.color * 0.5), self.color, int(self.color * 0.5))
                        elif self.matrix[row][col][0] == 1 and self.matrix[row][col][1] < self.length:
                            self.matrix[row][col][1] += 1
                            self.sense.set_pixel(col, row, 0, self.color, 0)
                        elif self.matrix[row][col][0] == 1 and self.matrix[row][col][1] == self.length:
                            self.matrix[row][col][1] += 1
                            self.sense.set_pixel(col, row, 0, int(self.color * 0.5), 0)
                        else:
                            self.matrix[row][col] = [0, 0]
                            self.sense.set_pixel(col, row, 0, 0, 0)
                else:
                    for col in range(8):
                        if not self.matrix[row][col][0] and self.matrix[row - 1][col] == [1, 0]:
                            pass
                        elif self.matrix[row][col][0] == 0 and self.matrix[row - 1][col][0] == 1:
                            self.matrix[row][col] = [1, 0]
                            self.sense.set_pixel(col, row, int(self.color * 0.5), self.color, int(self.color * 0.5))
                        elif self.matrix[row][col][0] == 1 and self.matrix[row][col][1] < self.length:
                            self.matrix[row][col][1] += 1
                            self.sense.set_pixel(col, row, 0, self.color, 0)
                        elif self.matrix[row][col][0] == 1 and self.matrix[row][col][1] == self.length:
                            self.matrix[row][col][1] += 1
                            self.sense.set_pixel(col, row, 0, int(self.color * 0.5), 0)
                        else:
                            self.matrix[row][col] = [0, 0]
                            self.sense.set_pixel(col, row, 0, 0, 0)
            completed_cycles += 1
            if completed_cycles >= self.cycles and self.cycles != 0:
                break

            time.sleep(self.refresh)


if __name__ == "__main__":
    THE_MATRIX = Matrix()
    THE_MATRIX.enter()
