#!/usr/bin/env python

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
    environment.set_color_from_temp()
    environment.display_environment()
    fly.catch()
    seizure.seize()
