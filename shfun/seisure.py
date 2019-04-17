#!/usr/bin/env python
import random
import time

from sense_hat import SenseHat


class Seisure:
    """Help an epileptic have a seisure
    Attributes:
        rotation    how is your pi oriented?
        speed       how fast should the pixels change?
        cycles      how many iterations to run (0 to run forever)
    """

    def __init__(
            self,
            rotation=0,
            speed=0.01,
            cycles=0,
    ):

        self.speed = speed
        self.cycles = cycles

        self.sense = SenseHat()
        self.sense.set_rotation(rotation)
        self.sense.clear()

    def seize(self):
        previous_pixel = (0, 0)
        completed_cycles = 0
        while True:
            rng = random.SystemRandom()
            x = int(rng.getrandbits(3))
            y = int(rng.getrandbits(3))
            r = int(rng.getrandbits(8))
            g = int(rng.getrandbits(8))
            b = int(rng.getrandbits(8))

            self.sense.set_pixel(*(previous_pixel + (0, 0, 0)))
            self.sense.set_pixel(x, y, r, g, b)
            previous_pixel = (x, y)
            time.sleep(self.speed)

            completed_cycles += 1
            if completed_cycles >= self.cycles != 0:
                self.sense.clear()
                break


if __name__ == "__main__":
    SEISURE = Seisure()
    SEISURE.seize()
