#!/usr/bin/env python
import time

from shfun import matrix
from shfun import environment
from shfun import fly
from shfun import seisure

the_matrix = matrix.Matrix(cycles=10000)
environment = environment.Environment(cycles=3)
fly = fly.Fly(cycles=25)
seisure = seisure.Seisure(cycles=10000)

while True:
    the_matrix.enter()
    time.sleep(1)
    environment.set_color_from_temp()
    environment.display_environment()
    time.sleep(1)
    fly.catch()
    time.sleep(1)
    seisure.seize()
    time.sleep(1)
