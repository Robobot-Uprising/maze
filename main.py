#!/usr/bin/env python3

from ev3dev.ev3 import ColorSensor
from time import sleep

# Connect to sensor
sensor = ColorSensor()

sensor.mode = 'COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')

while True:
  print(colors[sensor.value()])
  sleep(0.5)
