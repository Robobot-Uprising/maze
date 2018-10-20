#!/usr/bin/env python3

from ev3dev.ev3 import ColorSensor
from time import sleep

# Connect to sensor
sensor = ColorSensor()

sensor.mode = 'COL-REFLECT'

while True:
  print(sensor.value())
  sleep(0.5)
