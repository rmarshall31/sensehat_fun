#!/usr/bin/env python
import time

from shfun import environment
from shfun import fly
from shfun import hai_retirement
from shfun import matrix
from shfun import seizure

the_matrix = matrix.Matrix(cycles=10000)
environment = environment.Environment(cycles=3)
fly = fly.Fly(cycles=25)
seizure = seizure.Seizure(cycles=10000)
general = hai_retirement.General()

while True:
    the_matrix.enter()
    time.sleep(1)
    environment.set_color_from_temp()
    environment.display_environment()
    time.sleep(1)
    fly.catch()
    time.sleep(1)
    seizure.seize()
    time.sleep(1)
    general.days_to_retirement()
    time.sleep(1)
