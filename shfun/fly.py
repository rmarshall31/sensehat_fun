#!/usr/bin/env python
import random
import time

from sense_hat import SenseHat


class Fly:
    """Help a fly randomly find a flower
    Attributes:
        rotation    how is your pi oriented?
        speed       how fast will the fly hunt for the flower?
        cycles      how many flowers to find (0 to run forever)
        color       color of the fly
    """

    def __init__(
            self,
            rotation=0,
            speed=0.05,
            cycles=0,
            color=[30, 0, 150],
    ):

        self.color = color
        self.speed = speed
        self.cycles = cycles

        self.sense = SenseHat()
        self.sense.set_rotation(rotation)
        self.sense.clear()

    def print_pos(self, position, color):
        self.sense.set_pixel(int(position % 8), int(position / 8), color)

    def clear_pos(self, position):
        self.sense.set_pixel(int(position % 8), int(position / 8), 0, 0, 0)

    def catch(self):
        flower = random.randint(0, 63)
        pos = random.randint(0, 63)
        oldpos = 0

        self.print_pos(flower, (90, 90, 0))

        completed_cycles = 0
        while True:
            moved = False
            self.clear_pos(oldpos)
            if flower == oldpos:
                completed_cycles += 1
                if completed_cycles >= self.cycles != 0:
                    self.sense.clear()
                    break
                flower = random.randint(0, 63)
                self.print_pos(flower, [90, 90, 0])
            oldpos = pos
            self.print_pos(pos, self.color)
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
                    if pos not in [y * 8 for y in range(8)]:
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

            time.sleep(self.speed)


if __name__ == "__main__":
    FLY = Fly()
    FLY.catch()
